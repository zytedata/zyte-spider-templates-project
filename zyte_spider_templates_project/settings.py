from itemadapter import ItemAdapter
from zyte_common_items import ZyteItemAdapter

ItemAdapter.ADAPTER_CLASSES.appendleft(ZyteItemAdapter)

BOT_NAME = "zyte_spider_templates_project"

SPIDER_MODULES = [
    "zyte_spider_templates.spiders",
    "zyte_spider_templates_project.spiders",
]
NEWSPIDER_MODULE = "zyte_spider_templates_project.spiders"

CLOSESPIDER_TIMEOUT_NO_ITEM = 600
ADDONS = {
    "scrapy_zyte_api.Addon": 500,
}
SCHEDULER_DISK_QUEUE = "scrapy.squeues.PickleFifoDiskQueue"
SCHEDULER_MEMORY_QUEUE = "scrapy.squeues.FifoMemoryQueue"
SPIDER_MIDDLEWARES = {
    "scrapy_poet.RetryMiddleware": 275,
    "scrapy.spidermiddlewares.offsite.OffsiteMiddleware": None,
    "zyte_spider_templates.middlewares.AllowOffsiteMiddleware": 500,
    "zyte_spider_templates.middlewares.CrawlingLogsMiddleware": 1000,
}

# scrapy-poet
SCRAPY_POET_DISCOVER = [
    "zyte_spider_templates.pages",
    "zyte_spider_templates_project.pages",
]
