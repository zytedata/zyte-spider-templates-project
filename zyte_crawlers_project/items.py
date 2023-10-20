from typing import Optional

import attrs
from zyte_common_items import Product


@attrs.define
class Book(Product):
    stock: Optional[int]
