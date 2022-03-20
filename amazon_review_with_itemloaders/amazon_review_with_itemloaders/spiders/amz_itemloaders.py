import scrapy
from itemloaders import ItemLoader
from amazon_review_with_itemloaders.items import ReviewItem

base_asin_url = 'https://www.amazon.com/product-reviews/{}'

#scrapy crawl amz_itemloaders -O amz.csv -a asin=B07PGL8J8G
class AmzItemloadersSpider(scrapy.Spider):
    name = 'amz_itemloaders'
    def start_requests(self):
        asin = getattr(self, 'asin', None)
        if asin is not None:
            asin_url = base_asin_url.format(asin)
            yield scrapy.Request(asin_url)

    def parse(self, response):
        for review in response.xpath('//div[@data-hook="review"]'):
            loader = ItemLoader(item=ReviewItem(),selector=review)

            rating_xpath = './/*[contains(@data-hook,"review-star-rating")]/span/text()'
            title_xpath = './/*[@data-hook="review-title"]/span/text()'
            loc_time_xpath = './/*[@data-hook="review-date"]/text()'
            review_xpath ='normalize-space(.//*[@data-hook="review-body"]/span)'
            
            loader.add_xpath('rating', rating_xpath) #input processor is called with add_xpath
            loader.add_xpath('title', title_xpath)
            loader.add_xpath('country_region', loc_time_xpath)
            loader.add_xpath('date', loc_time_xpath)
            loader.add_xpath('review', review_xpath)
            loader.add_value('page_url', response.url)

            item = loader.load_item() #output processor is called
            yield item

        next_page = response.xpath('//a[contains(text(),"Next page")]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)