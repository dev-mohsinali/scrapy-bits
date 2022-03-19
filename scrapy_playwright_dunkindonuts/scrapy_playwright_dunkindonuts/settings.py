BOT_NAME = 'scrapy_playwright_dunkindonuts'
SPIDER_MODULES = ['scrapy_playwright_dunkindonuts.spiders']
NEWSPIDER_MODULE = 'scrapy_playwright_dunkindonuts.spiders'
ROBOTSTXT_OBEY = True
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
