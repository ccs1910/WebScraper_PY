# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.exceptions import DropItem
import time

class CsvWriterPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
    
    def spider_opened(self, spider):
        filename = "output_m123_"+time.strftime("%Y%m%d-%H%M%S")
        self.file = open(filename+'.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()
    
    
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
        

class PricePipeline(object):

    vat_factor = 1.15

    def process_item(self, item, spider):
        if item['price']:
#             if item['price_excludes_vat']:
#                 item['price'] = item['price'] * self.vat_factor
            #change to integer
            item['price'] = int(item['price'].strip("Rp").strip().replace(".",""))
            return item
        else:
            raise DropItem("Missing price in %s" % item)