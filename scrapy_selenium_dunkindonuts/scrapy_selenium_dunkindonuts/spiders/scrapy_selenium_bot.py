import scrapy
import time
from scrapy_selenium import SeleniumRequest

def wait(driver):
    time.sleep(1)
    return True
# get addresses of dunkindonuts based on location
class ScrapySeleniumBotSpider(scrapy.Spider):
    name = 'scrapy_selenium_bot'
    allowed_domains = ['dunkindonuts.com']
    start_urls = ['https://www.dunkindonuts.com/en/locations?location=02110']

    def start_requests(self):
        yield SeleniumRequest(url = self.start_urls[0], wait_time=10,wait_until=wait)

    def parse(self, response):
        for address in response.xpath('//div/ul[@class="store-item__list js-store-list"]/li'):
            item = {
                'address_line_1': address.xpath('.//div[@class="store-item__address js-store-address"]/div[@class="store-item__address--line1"]/a/text()').get(),
                'address_line_2': address.xpath('.//div[@class="store-item__address js-store-address"]/div[@class="store-item__address--line3"]/text()').get(),
                'phone': address.xpath('.//div[@class="store-item__contacts js-store-contacts"]/a/text()').get(),
            }
            yield item
