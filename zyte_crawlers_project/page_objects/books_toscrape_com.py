import re

from web_poet import Returns, field, handle_urls
from zyte_common_items import AutoProductPage

from ..items import Book


@handle_urls("books.toscrape.com")
class BookPage(AutoProductPage, Returns[Book]):
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
