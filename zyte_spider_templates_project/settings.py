from itemadapter import ItemAdapter
from zyte_common_items import ZyteItemAdapter

ItemAdapter.ADAPTER_CLASSES.appendleft(ZyteItemAdapter)

BOT_NAME = "zyte_spider_templates_project"

SPIDER_MODULES = [
    "zyte_spider_templates.spiders",
    "zyte_spider_templates_project.spiders",
]
NEWSPIDER_MODULE = "zyte_spider_templates_project.spiders"

CLOSESPIDER_TIMEOUT_NO_ITEM = 900
ADDONS = {
    "zyte_spider_templates.Addon": 100,
    "scrapy_zyte_api.Addon": 500,
    "duplicate_url_discarder.Addon": 600,
}

SCHEDULER_DISK_QUEUE = "scrapy.squeues.PickleFifoDiskQueue"
SCHEDULER_MEMORY_QUEUE = "scrapy.squeues.FifoMemoryQueue"
SCHEDULER_PRIORITY_QUEUE = "scrapy.pqueues.DownloaderAwarePriorityQueue"

DOWNLOADER_MIDDLEWARES = {
    "scrapy_poet.InjectionMiddleware": 543,
    "scrapy_zyte_api.ScrapyZyteAPIDownloaderMiddleware": 1000,
    "zyte_spider_templates.middlewares.MaxRequestsPerSeedDownloaderMiddleware": 100,
}

SPIDER_MIDDLEWARES = {
    "scrapy_poet.RetryMiddleware": 275,
    "scrapy.spidermiddlewares.offsite.OffsiteMiddleware": None,
    "zyte_spider_templates.IncrementalCrawlMiddleware": 45,
    "zyte_spider_templates.middlewares.OffsiteRequestsPerSeedMiddleware": 49,
    "zyte_spider_templates.middlewares.OnlyFeedsMiddleware": 108,
    "zyte_spider_templates.middlewares.TrackNavigationDepthSpiderMiddleware": 110,
    "scrapy_zyte_api.ScrapyZyteAPISpiderMiddleware": 100,
    "zyte_spider_templates.middlewares.AllowOffsiteMiddleware": 500,
    "zyte_spider_templates.middlewares.TrackSeedsSpiderMiddleware": 550,
    "zyte_spider_templates.middlewares.CrawlingLogsMiddleware": 1000,
}
# scrapy-poet
SCRAPY_POET_DISCOVER = [
    "zyte_spider_templates.pages",
    "zyte_spider_templates_project.pages",
]

ITEM_PIPELINES = {"zyte_common_items.pipelines.DropLowProbabilityItemPipeline": 0}

ITEM_PROBABILITY_THRESHOLDS = {
    "zyte_common_items.items.Article": 0.1,
    "zyte_common_items.items.Product": 0.2,
}
# duplicate-url-discarder
DUD_ATTRIBUTES_PER_ITEM = {
    "zyte_common_items.Product": [
        "canonicalUrl",
        "brand",
        "name",
        "gtin",
        "mpn",
        "productId",
        "sku",
        "color",
        "size",
        "style",
    ],
    "zyte_common_items.Article": [
        "canonicalUrl",
        "headline",
        "datePublishedRaw",
        "authors",
    ],
}
