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
    "scrapy_zyte_api.Addon": 500,
    "duplicate_url_discarder.Addon": 600,
}
SCHEDULER_DISK_QUEUE = "scrapy.squeues.PickleFifoDiskQueue"
SCHEDULER_MEMORY_QUEUE = "scrapy.squeues.FifoMemoryQueue"
SPIDER_MIDDLEWARES = {
    "scrapy_poet.RetryMiddleware": 275,
    "scrapy.spidermiddlewares.offsite.OffsiteMiddleware": None,
    "zyte_spider_templates.middlewares.AllowOffsiteMiddleware": 500,
    "zyte_spider_templates.middlewares.CrawlingLogsMiddleware": 1000,
}
EXTENSIONS = {
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}

# scrapy-poet
SCRAPY_POET_DISCOVER = [
    "zyte_spider_templates.pages",
    "zyte_spider_templates_project.pages",
]

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
        "style"
    ],
}

# spidermon
SPIDERMON_SPIDER_CLOSE_MONITORS = (
    "zyte_spider_templates_project.monitors.CustomSpiderCloseMonitorSuite",
)
SPIDERMON_MAX_ERRORS = 0
SPIDERMON_ADD_FIELD_COVERAGE = True
SPIDERMON_FIELD_COVERAGE_RULES = {
    "Product/url": 1.0,
    "Product/name": 1.0,
    "Product/metadata": 1.0,
}
SPIDERMON_ITEM_COUNT_INCREASE = 1  # At least 1 item every 5 minutes
SPIDERMON_PERIODIC_MONITORS = {
   'spidermon.contrib.scrapy.monitors.PeriodicItemCountMonitorSuite': 500,
}
SPIDERMON_UNWANTED_HTTP_CODES = {
    400: {"max_percentage": 0.3},
    500: {"max_percentage": 0.2},
}
