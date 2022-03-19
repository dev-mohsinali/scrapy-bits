import scrapy
from scrapy_playwright.page import PageCoroutine

class ScrapyPlaywrightShoppableSpider(scrapy.Spider):
   
    name = 'scrapy_playwright_shoppable'
    def start_requests(self):
        yield scrapy.Request(url = 'https://shoppable-campaign-demo.netlify.app/#/',
        meta = dict(playwright= True,
        playwright_include_page= True,
        playwright_page_coroutines= 
        [PageCoroutine ('wait_for_selector','div#productListing')]
        ))
        
    async def parse(self, response):
        yield {
            'text': response.text
        }