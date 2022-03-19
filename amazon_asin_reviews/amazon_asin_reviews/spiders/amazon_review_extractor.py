import scrapy

base_asin_url = 'https://www.amazon.com/product-reviews/{}'

#scrapy crawl amazon_review_extractor -O amz.csv -a asin=B07PGL8J8G
class AmazonSpider(scrapy.Spider):
    name='amazon_review_extractor'
    def start_requests(self):
        asin = getattr(self, 'asin', None)
        if asin is not None:
            asin_url = base_asin_url.format(asin)
            yield scrapy.Request(asin_url)

    def parse(self, response):
        for review in response.xpath('//div[@data-hook="review"]'):
            item = {
                'rating': review.xpath('.//*[contains(@data-hook,"review-star-rating")]/span/text()').get(),
                'title': review.xpath('.//*[@data-hook="review-title"]/span/text()').get(),
                'loc_time': review.xpath('.//*[@data-hook="review-date"]/text()').get(),
                'review': review.xpath('normalize-space(.//*[@data-hook="review-body"]/span)').get(),
                'page_url':response.url
            }
            yield item
        next_page = response.xpath('//a[contains(text(),"Next page")]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)