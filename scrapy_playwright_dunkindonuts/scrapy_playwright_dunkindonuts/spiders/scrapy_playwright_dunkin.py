import scrapy
from scrapy_playwright.page import PageCoroutine

class ScrapyPlaywrightDunkinSpider(scrapy.Spider):
    name = 'scrapy_playwright_dunkin'
    allowed_domains = ['dunkindonuts.com']
    start_urls = ['https://www.dunkindonuts.com/en/locations?location=02110']

    def start_requests(self):
        meta = dict(playwright= True,
        playwright_include_page= True,
        playwright_page_coroutines= 
        [PageCoroutine ('wait_for_selector','div.store-item__address--line3')]
        )
        yield scrapy.Request(url = self.start_urls[0],meta= meta)
        
    async def parse(self, response):
        for address in response.xpath('//div/ul[@class="store-item__list js-store-list"]/li'):
            item = {
                'address_line_1': address.xpath('.//div[@class="store-item__address js-store-address"]/div[@class="store-item__address--line1"]/a/text()').get(),
                'address_line_2': address.xpath('.//div[@class="store-item__address js-store-address"]/div[@class="store-item__address--line3"]/text()').get(),
                'phone': address.xpath('.//div[@class="store-item__contacts js-store-contacts"]/a/text()').get(),
            }
            yield item
