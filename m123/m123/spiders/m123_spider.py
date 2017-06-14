import scrapy
from scrapy.spider import BaseSpider as Spider

from scrapy.spider import CrawlSpider, Rule

from scrapy.loader import ItemLoader

from m123.items import M123Item

from scrapy.selector import Selector

from scrapy.linkextractors import LinkExtractor

class M123Spider(CrawlSpider):
    name = "m123"
    allowed_domains = ['mobil123.com']
    start_urls = ['https://www.mobil123.com/mobil-bekas-dijual/indonesia',]
        
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('li.next > a',)),
             callback="parse_item",
             follow=True),)
    
    
    def parse_item(self, response):
        
        
        self.logger.info('Starts : %s',response.url)
       
        sel = Selector(response)
#         results = sel.css('section#classified-listings-result > article')
        results = sel.xpath('//section[@id="classified-listings-result"]/article')
        items = []
           
        for result in results:
            item = M123Item()
            
            locationList = result.xpath('//div[i[contains(concat(" ",@class," "),"icon--location")]]/text()').extract()
            
            item['location'] = locationList[1].strip()
            
            item['year'] = result.css('::attr(data-year)').extract_first()#data[0]
            item['brand'] = result.css('::attr(data-make)').extract_first()#data[1]
            item['model'] = result.css('::attr(data-model)').extract_first()
            item['variant'] = ((result.css('::attr(data-display-title)').extract_first().strip()).split(" ",2))[2] #data[2] 
            
            item['discount'] = result.css('::attr(data-hot-deal)').extract_first()
  
            if item['discount'] == "false":
                item['price']=result.css('div.flexbox__item > div.listing__price::text').extract_first()
            else:
                item['price']=result.css('div.hot-deal div.listing__price > span.weight--semibold::text').extract_first()
              
            items.append(item)
              
        return items
        self.logger.info('ends')
        

            