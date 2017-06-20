import scrapy
from scrapy.spider import BaseSpider as Spider

from scrapy.spider import CrawlSpider, Rule

from rmob.items import RmobItem

from scrapy.selector import Selector

from scrapy.linkextractors import LinkExtractor

class RmobSpider(CrawlSpider):
    name = "rmob"
    allowed_domains = ['rajamobil.com']
    start_urls = ['https://www.rajamobil.com/jual/mobil/bekas?lokasi=jadetabek',]
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('li.next > a',)),
             callback="parse_item",
             follow=True),)
    
    def parse_item(self,response):
        self.logger.info('Starts : %s',response.url)
       
        sel = Selector(response)
        
        results = sel.xpath('//div[@id="wrapper-carimobil-container"]/div[@class="list-mobil"]')
        
        self.logger.info('Result Size : %d', len(results))
        
        items = []
        
        for result in results :
            item = RmobItem()
            
            
            item['id'] = result.css('a::attr(href)').extract_first()
            item['brand'] = result.css('h2.firstTitle::attr(title)').extract_first()
            item['full_title'] = result.css('h3.secondTitle::attr(title)').extract_first()
            item['year'] = result.css('h3.secondTitle::attr(title)').extract_first()[-4:]
            
            specs = result.css('ul.umum-spek > li::text').extract()
            item['transmission'] = specs[2] 
            item['price'] = result.css('div.thirdTitle > b::text').extract_first()
            
            items.append(item)
              
        return items
        self.logger.info('ends')
        
    parse_start_url = parse_item
