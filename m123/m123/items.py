# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class M123Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    listing_id = Field()
    year = Field()
    brand = Field()
    model = Field()
    title = Field()
    price = Field()
    location = Field()
    discount = Field()
    transmission = Field()