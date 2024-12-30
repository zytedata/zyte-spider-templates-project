from logging import INFO

from itemadapter import ItemAdapter
from scrapy.logformatter import LogFormatter, DROPPEDMSG
from zyte_common_items import ZyteItemAdapter

ItemAdapter.ADAPTER_CLASSES.appendleft(ZyteItemAdapter)

BOT_NAME = "zyte_spider_templates_project"

SPIDER_MODULES = [
    "zyte_spider_templates.spiders",
    "zyte_spider_templates_project.spiders",
]

NEWSPIDER_MODULE = "zyte_spider_templates_project.spiders"

ADDONS = {
    "scrapy_zyte_api.Addon": 500,
    "duplicate_url_discarder.Addon": 600,
    "zyte_spider_templates.Addon": 700,
}
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.stats.DownloaderStats": None,
    "scrapy_poet.DownloaderStatsMiddleware": 850,
}
SPIDER_MIDDLEWARES = {
    "scrapy_poet.RetryMiddleware": 275,
}


class CustomLogFormatter(LogFormatter):
    def dropped(self, item, exception, response, spider):
        return {
            'level': INFO,
            'msg': DROPPEDMSG,
            'args': {
                'exception': exception,
                'item': item,
            }
        }


LOG_FORMATTER = CustomLogFormatter


# scrapy-poet
SCRAPY_POET_DISCOVER = [
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
        "style",
    ],
    "zyte_common_items.Article": [
        "canonicalUrl",
        "headline",
        "datePublishedRaw",
        "authors",
    ],
}
