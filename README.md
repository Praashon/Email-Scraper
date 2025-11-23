# Email Scraper 📧

> A powerful web scraping tool built with Scrapy to extract email addresses from websites efficiently and ethically.

## What Does It Do?

Ever needed to collect contact information from multiple websites for legitimate business purposes? Email Scraper automates this process using Python and Scrapy, crawling through web pages to find and extract email addresses. Perfect for researchers, marketers, and data analysts who need to gather public contact information at scale.

## Features That Make It Stand Out

- **Smart Crawling** - Intelligently navigates through website structures to find email addresses
- **Pattern Recognition** - Uses advanced regex patterns to identify valid email formats
- **Scalable Architecture** - Built on Scrapy, one of the most powerful scraping frameworks
- **Customizable** - Easily configure domains, depth limits, and crawl rules
- **Export Options** - Save results in various formats (CSV, JSON, TXT)
- **Respectful Scraping** - Includes rate limiting and robots.txt compliance

## Tech Stack

- **Python 3.13** - Modern Python for optimal performance
- **Scrapy 2.12+** - Industrial-strength web scraping framework
- **Twisted** - Asynchronous networking engine
- **beautifulsoup4** - HTML parsing when needed
- **regex** - Advanced pattern matching for emails

## Getting Started

### Prerequisites

Make sure you have Python 3.8 or higher installed on your system.

### Installation

1. **Clone or download this repository**
   ```bash
   cd EmailScraper
   ```

2. **Create and activate a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install scrapy
   pip install -r requirements.txt
   ```

## How to Use

### Basic Usage

1. **Navigate to the Scrapy project directory**
   ```bash
   cd EmailScraperWeb
   ```

2. **Run the spider**
   ```bash
   scrapy crawl EmailScrape -o emails.csv
   ```

3. **Check your results**
   The scraped emails will be saved in `emails.csv` in your current directory.

### Advanced Configuration

You can customize the scraping behavior by modifying the spider settings:

- **Change output format**: Use `-o emails.json` or `-o emails.txt`
- **Set crawl depth**: Modify `DEPTH_LIMIT` in `settings.py`
- **Adjust politeness**: Configure `DOWNLOAD_DELAY` to be respectful to servers
- **Filter domains**: Edit allowed domains in the spider file

## Project Structure

```
EmailScraper/
├── EmailScraperWeb/          # Main Scrapy project
│   └── EmailScraperWeb/
│       ├── spiders/          # Spider definitions
│       │   └── EmailScrape.py
│       ├── settings.py       # Scrapy configuration
│       └── __init__.py
├── venv/                     # Virtual environment
├── .gitignore               # Git ignore rules
└── README.md                # You are here!
```

## Important Notes

### Legal & Ethical Considerations

⚠️ **Use Responsibly**: This tool should only be used for legitimate purposes:
- Always respect website Terms of Service
- Check and comply with robots.txt
- Don't overload servers with requests
- Only scrape publicly available information
- Comply with GDPR, CAN-SPAM, and other data protection laws

### Best Practices

1. **Set reasonable delays** between requests (1-2 seconds minimum)
2. **Limit concurrent requests** to avoid server overload
3. **Use a user agent** that identifies your scraper
4. **Keep logs** of what you've scraped and when
5. **Store data securely** and delete it when no longer needed

## Troubleshooting

### Common Issues

**Spider not found?**
- Make sure you're in the correct directory (`EmailScraperWeb`)
- Check that your spider file exists in the `spiders/` folder

**No emails found?**
- The target website might use JavaScript rendering
- Emails might be obfuscated or protected
- Check your regex patterns are correct

**Import errors?**
- Ensure your virtual environment is activated
- Reinstall dependencies with `pip install -r requirements.txt`

## Configuration Tips

### Customize Your Scraping

Edit `EmailScraperWeb/EmailScraperWeb/settings.py`:

```python
# Be polite - wait between requests
DOWNLOAD_DELAY = 2

# Identify yourself
USER_AGENT = 'EmailScraper (+http://yourwebsite.com)'

# Respect robots.txt
ROBOTSTXT_OBEY = True

# Limit crawl depth
DEPTH_LIMIT = 3
```

## Future Enhancements

- [ ] Add duplicate email detection
- [ ] Implement database storage
- [ ] Create GUI interface
- [ ] Add email validation API integration
- [ ] Support for JavaScript-heavy sites
- [ ] Export to Excel format
- [ ] Add scheduling capabilities

## Contributing

Found a bug? Have an idea? Contributions are welcome! Feel free to:
- Open an issue
- Submit a pull request
- Suggest new features

## Learning Resources

New to web scraping? Check out:
- [Scrapy Official Documentation](https://docs.scrapy.org/)
- [Web Scraping Best Practices](https://www.scrapehero.com/web-scraping-best-practices/)
- [Python Regex Tutorial](https://docs.python.org/3/howto/regex.html)

## License

This project is intended for educational and legitimate business purposes only. Users are responsible for ensuring their use complies with all applicable laws and regulations.

---

**Built with 💻 by Praashon Gautam**

*Remember: With great scraping power comes great responsibility. Always scrape ethically!*
