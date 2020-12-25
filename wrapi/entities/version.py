from __future__ import annotations

from ..types_.entity import BaseEntity


class Version(BaseEntity):
    major: int
    minor: int
