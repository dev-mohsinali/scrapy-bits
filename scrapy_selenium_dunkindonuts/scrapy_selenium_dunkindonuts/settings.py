BOT_NAME = 'scrapy_selenium_dunkindonuts'
SPIDER_MODULES = ['scrapy_selenium_dunkindonuts.spiders']
NEWSPIDER_MODULE = 'scrapy_selenium_dunkindonuts.spiders'
ROBOTSTXT_OBEY = True
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'cache-control':'max-age=0'
}
AUTOTHROTTLE_ENABLED= True
AUTOTHROTTLE_TARGET_CONCURRENCY= 2
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = 'D:\chromedriver.exe'
SELENIUM_DRIVER_ARGUMENTS=[]  # '--headless' if using chrome instead of firefox
COOKIES_ENABLED = True
COOKIES_DEBUG = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}