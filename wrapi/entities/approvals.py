from __future__ import annotations

from datetime import date, datetime
from typing import Optional, Sequence

from ..types_.entity import BaseEntity
from ..types_.outputs import ApprovalDecision, ApprovalType
from ..types_.scalar import (
    AttachmentId,
    ContactId,
    FolderId,
    TaskId,
)


class Approval(BaseEntity):
    task_id: Optional[TaskId]
    folder_id: Optional[FolderId]
    author_id: ContactId
    title: str
    description: str
    updated_date: datetime
    due_date: date
    decisions: Sequence[ApprovalDecision]
    attachment_ids: Optional[Sequence[AttachmentId]]
    type: ApprovalType
    auto_finish_on_approve: bool
    auto_finish_on_reject: bool
    finished: bool
    finisher_id: Optional[ContactId]
