BOT_NAME = "zyte_spider_templates_project"

SPIDER_MODULES = [
    "zyte_spider_templates.spiders",
    "zyte_spider_templates_project.spiders",
]
NEWSPIDER_MODULE = "zyte_spider_templates_project.spiders"

CLOSESPIDER_TIMEOUT_NO_ITEM = 600
DOWNLOAD_HANDLERS = {
    "http": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
    "https": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
}
DOWNLOADER_MIDDLEWARES = {
    "scrapy_poet.InjectionMiddleware": 543,
    "scrapy_zyte_api.ScrapyZyteAPIDownloaderMiddleware": 1000,
}
REQUEST_FINGERPRINTER_CLASS = "scrapy_zyte_api.ScrapyZyteAPIRequestFingerprinter"
SCHEDULER_DISK_QUEUE = "scrapy.squeues.PickleFifoDiskQueue"
SCHEDULER_MEMORY_QUEUE = "scrapy.squeues.FifoMemoryQueue"
SPIDER_MIDDLEWARES = {
    "scrapy_poet.RetryMiddleware": 275,
    "zyte_spider_templates.middlewares.CrawlingLogsMiddleware": 1000,
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# scrapy-poet
SCRAPY_POET_DISCOVER = [
    "zyte_spider_templates.page_objects",
    "zyte_spider_templates_project.page_objects",
]
SCRAPY_POET_PROVIDERS = {
    "scrapy_zyte_api.providers.ZyteApiProvider": 1100,
}

# scrapy-zyte-api
ZYTE_API_TRANSPARENT_MODE = True
