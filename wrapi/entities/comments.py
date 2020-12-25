from __future__ import annotations

from datetime import datetime
from typing import Optional

from ..types_.entity import BaseEntity
from ..types_.scalar import CommentId, ContactId


class Comment(BaseEntity):
    id: CommentId
    author_id: ContactId
    text: str
    created_date: datetime
    task_id: str
    folder_id: Optional[str]
