import re

from web_poet import Returns, field, handle_urls
from zyte_common_items import AutoProductPage

from ..items import CustomProduct


@handle_urls("ao.com")
class AoComPage(AutoProductPage, Returns[CustomProduct]):
    @field
    async def epc(self):
        match = re.search(r"\b[A-G]\+?\+?(?=[\s-]*[Rr]at(ed|ing)\b)", await self.name)
        return match[0] if match else None
