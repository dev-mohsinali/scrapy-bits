BOT_NAME = 'amazon_asin_reviews'
SPIDER_MODULES = ['amazon_asin_reviews.spiders']
NEWSPIDER_MODULE = 'amazon_asin_reviews.spiders'
ROBOTSTXT_OBEY = True
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'cache-control':'max-age=0'
}
AUTOTHROTTLE_ENABLED= True
AUTOTHROTTLE_TARGET_CONCURRENCY= 2
