import re

import attrs
from number_parser import parse_number
from web_poet import BrowserResponse, Returns, field, handle_urls
from zyte_common_items import AggregateRating, AutoProductPage

from ..items import Book


@handle_urls("books.toscrape.com")
@attrs.define
class BookPage(AutoProductPage, Returns[Book]):
    response: BrowserResponse

    @field
    async def aggregateRating(self):
        element_class = self.response.css(".star-rating::attr(class)").get()
        if not element_class:
            return None
        rating_str = element_class.split(" ")[-1]
        rating = parse_number(rating_str)
        if not rating:
            return None
        return AggregateRating(ratingValue=rating, bestRating=5)

    @field
    async def stock(self):
        for entry in await self.additionalProperties:
            if entry.name == "availability":
                match = re.search(r"\d([.,\s]*\d+)*(?=\s+available\b)", entry.value)
                if not match:
                    return None
                stock_str = re.sub(r"[.,\s]", "", match[0])
                return int(stock_str)
        return None
