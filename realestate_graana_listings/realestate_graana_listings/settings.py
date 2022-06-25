BOT_NAME = 'realestate_graana_listings'
SPIDER_MODULES = ['realestate_graana_listings.spiders']
NEWSPIDER_MODULE = 'realestate_graana_listings.spiders'
ROBOTSTXT_OBEY = True
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'cache-control':'max-age=0'
}
AUTOTHROTTLE_ENABLED= True
AUTOTHROTTLE_TARGET_CONCURRENCY= 2
ITEM_PIPELINES = {
    'realestate_graana_listings.pipelines.RealestateGraanaListingsPipeline': 300
}