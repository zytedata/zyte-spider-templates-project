from itemadapter import ItemAdapter
from zyte_common_items import ZyteItemAdapter

ItemAdapter.ADAPTER_CLASSES.appendleft(ZyteItemAdapter)

BOT_NAME = "zyte_spider_templates_project"

SPIDER_MODULES = [
    "zyte_spider_templates_project.spiders",
]
NEWSPIDER_MODULE = "zyte_spider_templates_project.spiders"

ADDONS = {
    "zyte_spider_templates.Addon": 100,
    "scrapy_zyte_api.Addon": 500,
    "duplicate_url_discarder.Addon": 600,
}

SPIDER_MIDDLEWARES = {
    "scrapy_poet.RetryMiddleware": 275,
}

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
