import scrapy
from scrapy.spider import BaseSpider as Spider

from scrapy.spider import CrawlSpider, Rule

from scrapy.loader import ItemLoader
from mobil123.items import Mobil123Item

from scrapy.selector import Selector

from scrapy.linkextractors import LinkExtractor

class Mobil123Spider(CrawlSpider):
    name = "mobil123"
    allowed_domains = ['mobil123.com']
    start_urls = ['https://www.mobil123.com/mobil-bekas-dijual/indonesia',]
        
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('li.next > a',)),
             callback="parse_item",
             follow=True),)
    
    
    def parse_item(self, response):
        
        
        self.logger.info('Starts : %s',response.url)
       
        sel = Selector(response)
        results = sel.css('section#classified-listings-result > article')
        items = []
           
        for result in results:
            item = Mobil123Item()
          
            name = result.css('h2 > a::text').extract_first().strip()
            data = name.split(" ",2)
  
            item['year'] = data[0]
            item['brand'] = data[1]
            item['variant'] = data[2] 
  
            price = result.css('div.flexbox__item > div.listing__price::text').extract_first()
              
            if price:
                item['price']=price
                item['discount']="no"
            else:
                price = result.css('div.hot-deal div.listing__price > span.weight--semibold::text').extract_first()
                item['price']=price
                item['discount']="yes"
              
            items.append(item)
              
        return items
        self.logger.info('ends')
        

            