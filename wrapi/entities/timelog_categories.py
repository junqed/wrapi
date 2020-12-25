from __future__ import annotations

from ..types_.entity import BaseEntity
from ..types_.scalar import TimelogCategoryId


class TimelogCategory(BaseEntity):
    id: TimelogCategoryId
    name: str
    order: int
    hidden: bool
