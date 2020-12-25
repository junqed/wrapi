from __future__ import annotations

from ..types_.entity import BaseEntity


class Color(BaseEntity):
    name: str
    hex: str
