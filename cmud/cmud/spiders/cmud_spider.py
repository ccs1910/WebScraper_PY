import scrapy
from scrapy.spiders import BaseSpider as Spider

from cmud.items import CmudItem

from scrapy.selector import Selector
from hypothesis.strategies import none

from scrapy.exceptions import CloseSpider
from scrapy.signals import spider_closed


URL_BASE = "https://www.carmudi.co.id/cars/used/location:jakarta+indonesia/distance:100km/latitude:-6.17511/longitude:106.86503949999997/?sort=newest"
PAGES = range(1, 1001)
URL_LIST = map(lambda page: "%s&page=%d" % (URL_BASE, page), PAGES)


class CmudSpider(Spider):
    name = "cmud"
    allowed_domains = ['www.carmudi.co.id']
    start_urls = URL_LIST
    
    def parse(self, response):
        
        self.logger.info('Starts : %s',response.url)
        
        sel = Selector(response)
        
        results = sel.xpath('//section[contains(concat(" ",@class," "),"catalog-listing")]/div[contains(concat(" ",@class," "),"catalog-listing-item")]')
        items = []
        
        for result in results :
            item = CmudItem()
             
            #get Year, Brand & Model
             
            item['id'] = result.css('h3.item-title > a::attr(data-layer-label)').extract_first()
             
            title = (result.css('h3.item-title > a::text').extract_first().strip()).split(" ",2)
             
            item['year'] = title[0]            
            item['brand'] = title[1]    
            item['model'] = title[2]    
             
            item['price'] = result.css('h4.item-price > a::text').extract_first()
            
            item['transmission'] = result.xpath('//div/ul/li[i[@class="icon-gearshift"]]/span/text()').extract_first().strip()
             
            item['location'] = result.xpath('//div/p[i[@class="icon-location"]]/span/text()').extract_first().strip()
                 
            items.append(item)
            
            
        self.logger.info('ends')
        
        return items
        
        