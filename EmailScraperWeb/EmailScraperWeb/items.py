# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EmailItem(scrapy.Item):
    """Item class for storing scraped email information"""
    email = scrapy.Field()
    source_url = scrapy.Field()
    timestamp = scrapy.Field()
