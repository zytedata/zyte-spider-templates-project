from decimal import Decimal

from pydantic import Field
from scrapy_poet import DummyResponse
from scrapy_spider_metadata import Args

from ..items import Book
from ..zyte_crawlers.spiders.ecommerce import EcommerceSpider, EcommerceSpiderParams


class BooksToScrapeComTemplateParams(EcommerceSpiderParams):
    min_price: str = Field(
        title="Minimum price",
        default="0",
        pattern=r"^\d+(\.\d+)?$",
        strip_whitespace=True,
    )


class BooksToScrapeComTemplate(EcommerceSpider, Args[BooksToScrapeComTemplateParams]):
    name = "books_toscrape_com"
    metadata = {
        **EcommerceSpider.metadata,
        "title": "Books to Scrape",
        "description": "Template for books.toscrape.com",
    }

    def parse_product(self, response: DummyResponse, product: Book):
        if Decimal(product.price) < Decimal(self.args.min_price):
            self.logger.debug(
                f"Dropped due to low price ({product.price}): " f"{product}"
            )
            return
        yield product
