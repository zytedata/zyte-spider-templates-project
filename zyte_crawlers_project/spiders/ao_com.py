from scrapy_poet import DummyResponse

from ..items import CustomProduct
from ..zyte_crawlers.spiders.ecommerce import EcommerceSpider


class AoComTemplate(EcommerceSpider):
    name = "ao_com"
    metadata = {
        **EcommerceSpider.metadata,
        "title": "ao.com",
        "description": "Template for ao.com",
    }

    def parse_product(self, response: DummyResponse, product: CustomProduct):
        yield product
