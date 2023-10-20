from pydantic import Field
from scrapy_poet import DummyResponse
from scrapy_spider_metadata import Args

from ..items import Book
from ..zyte_crawlers.spiders.ecommerce import EcommerceSpider, EcommerceSpiderParams


class BooksToScrapeComTemplateParams(EcommerceSpiderParams):
    min_rating: int = Field(
        title="Minimum rating",
        default=0,
    )


class BooksToScrapeComTemplate(EcommerceSpider, Args[BooksToScrapeComTemplateParams]):
    name = "books_toscrape_com"
    metadata = {
        **EcommerceSpider.metadata,
        "title": "Books to Scrape",
        "description": "Template for books.toscrape.com",
    }

    def parse_product(self, response: DummyResponse, product: Book):
        if product.aggregateRating.ratingValue < self.args.min_rating:
            self.logger.debug(
                f"Dropped due to low rating ({product.aggregateRating.ratingValue}): "
                f"{product}"
            )
            return
        yield product
