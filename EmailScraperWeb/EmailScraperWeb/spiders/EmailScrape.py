import scrapy
import re
from datetime import datetime
from EmailScraperWeb.items import EmailItem


class EmailScrapeSpider(scrapy.Spider):
    """
    Spider for scraping email addresses from websites.
    
    Usage:
        scrapy crawl EmailScrape -o emails.csv
        scrapy crawl EmailScrape -a domain=example.com -o emails.json
    """
    
    name = "EmailScrape"
    
    # Email regex pattern - matches most common email formats
    email_pattern = re.compile(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    )
    
    def __init__(self, domain=None, *args, **kwargs):
        super(EmailScrapeSpider, self).__init__(*args, **kwargs)
        
        # If domain is provided as argument, use it
        if domain:
            self.allowed_domains = [domain]
            self.start_urls = [f'https://{domain}']
        else:
            # Default domains (modify as needed)
            self.allowed_domains = ['example.com']
            self.start_urls = ['https://example.com']
        
        self.logger.info(f"Starting email scraper for domains: {self.allowed_domains}")
    
    def parse(self, response):
        """
        Parse the response and extract emails.
        """
        # Extract text from the page
        page_text = ' '.join(response.css('*::text').getall())
        
        # Find all email addresses using regex
        emails = self.email_pattern.findall(page_text)
        
        # Also check in href attributes (mailto links)
        mailto_links = response.css('a[href^="mailto:"]::attr(href)').getall()
        for mailto in mailto_links:
            # Extract email from mailto:email@example.com
            email = mailto.replace('mailto:', '').split('?')[0]
            if email not in emails:
                emails.append(email)
        
        # Yield each unique email as an item
        for email in set(emails):
            item = EmailItem()
            item['email'] = email.lower().strip()
            item['source_url'] = response.url
            item['timestamp'] = datetime.now().isoformat()
            
            self.logger.info(f"Found email: {email} on {response.url}")
            yield item
        
        # Follow links to continue crawling (respecting depth limit in settings)
        for next_page in response.css('a::attr(href)').getall():
            if next_page:
                yield response.follow(next_page, callback=self.parse)
