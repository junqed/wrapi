from __future__ import annotations

from typing import Optional, Sequence

from ..types_.entity import BaseEntity
from ..types_.scalar import FolderBluePrintId


class FolderBlueprint(BaseEntity):
    id: FolderBluePrintId
    title: str
    child_ids: Optional[Sequence[FolderBluePrintId]]
    scope: str
