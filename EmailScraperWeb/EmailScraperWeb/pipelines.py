# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class EmailscraperwebPipeline:
    """Pipeline for processing scraped email items"""
    
    def __init__(self):
        self.emails_seen = set()
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Remove duplicates
        email = adapter.get('email')
        if email in self.emails_seen:
            raise DropItem(f"Duplicate email found: {email}")
        else:
            self.emails_seen.add(email)
            return item
