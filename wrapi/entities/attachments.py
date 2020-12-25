from __future__ import annotations

from datetime import datetime
from typing import Optional, Sequence

from pydantic.networks import AnyUrl

from ..types_.entity import BaseEntity
from ..types_.enums import AttachmentType
from ..types_.scalar import (
    AttachmentId,
    CommentId,
    ContactId,
    FolderId,
    ReviewId,
    TaskId,
)


class Attachment(BaseEntity):
    id: AttachmentId
    author_id: ContactId
    name: str
    created_date: datetime
    version: int
    type: AttachmentType
    content_type: str
    size: int
    task_id: Optional[TaskId]
    folder_id: Optional[FolderId]
    comment_id: Optional[CommentId]
    current_attachment_id: Optional[AttachmentId]
    preview_url: Optional[AnyUrl]
    url: Optional[AnyUrl]
    playlist_url: Optional[AnyUrl]
    review_ids: Optional[Sequence[ReviewId]]
    width: Optional[int]
    height: Optional[int]
