DOWNLOAD_HANDLERS = {
    "http": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
    "https": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
}
DOWNLOADER_MIDDLEWARES = {
    "scrapy_poet.InjectionMiddleware": 543,
    "scrapy_zyte_api.ScrapyZyteAPIDownloaderMiddleware": 1000,
}
REQUEST_FINGERPRINTER_CLASS = "scrapy_zyte_api.ScrapyZyteAPIRequestFingerprinter"
SPIDER_MIDDLEWARES = {
    "scrapy_poet.RetryMiddleware": 275,
}
SPIDER_MODULES = [
    "zyte_spider_templates_project.spiders",
    "zyte_crawlers.spiders",
]
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# scrapy-poet
SCRAPY_POET_DISCOVER = [
    "zyte_spider_templates_project.page_objects",
]
SCRAPY_POET_PROVIDERS = {
    "scrapy_zyte_api.providers.ZyteApiProvider": 1100,
}

# scrapy-zyte-api
ZYTE_API_TRANSPARENT_MODE = True
