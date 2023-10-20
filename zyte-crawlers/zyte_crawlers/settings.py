from itemadapter import ItemAdapter
from zyte_common_items import ZyteItemAdapter

ItemAdapter.ADAPTER_CLASSES.appendleft(ZyteItemAdapter)

BOT_NAME = "zyte_crawlers"

SPIDER_MODULES = ["zyte_crawlers.spiders"]
NEWSPIDER_MODULE = "zyte_crawlers.spiders"

ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    "scrapy_poet.InjectionMiddleware": 543,
    "scrapy_zyte_api.ScrapyZyteAPIDownloaderMiddleware": 1000,
}
SPIDER_MIDDLEWARES = {
    "scrapy_poet.RetryMiddleware": 275,
}

DOWNLOAD_HANDLERS = {
    "http": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
    "https": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
}
REQUEST_FINGERPRINTER_CLASS = "scrapy_zyte_api.ScrapyZyteAPIRequestFingerprinter"
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

SCRAPY_POET_PROVIDERS = {
    "scrapy_zyte_api.providers.ZyteApiProvider": 1100,
}

# ZYTE_API_KEY = "YOUR_API_KEY"

CLOSESPIDER_TIMEOUT_NO_ITEM = 600

SCHEDULER_DISK_QUEUE = "scrapy.squeues.PickleFifoDiskQueue"
SCHEDULER_MEMORY_QUEUE = "scrapy.squeues.FifoMemoryQueue"

SCRAPY_POET_DISCOVER = ["zyte_crawlers.page_objects.product_navigation_heuristics"]
