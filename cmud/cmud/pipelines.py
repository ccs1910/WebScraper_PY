# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.exceptions import DropItem
import time

# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         for field in item:
#             print field + ': ' + item[field][0]
#         return item


class CsvWriterPipeline(object):
    
    def __init__(self):
        self.files = {}
    
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
    
    def spider_opened(self, spider):
        filename = "output_cmud_"+time.strftime("%Y%m%d-%H%M%S")
        self.file = open(filename+'.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ["id","brand","model","transmission","year","location","price"]
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
        print('Starts : Process')
        if item['price']:
#             if item['price_excludes_vat']:
#                 item['price'] = item['price'] * self.vat_factor
            #change to integer
            if "juta" in item['price'].lower(): 
                item['price'] = float(item['price'].lower().replace("juta","").strip())*1000000
            elif "milyar" in item['price'].lower():
                item['price'] = float(item['price'].lower().replace("milyar","").strip())*1000000000
#             int(item['price'].strip("Rp").strip().replace(".",""))
                
            return item
        else:
            raise DropItem("Missing price in %s" % item)
        
