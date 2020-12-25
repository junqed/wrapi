from __future__ import annotations

from datetime import datetime
from typing import Optional, Sequence

from ..types_.entity import BaseEntity
from ..types_.enums import (
    BillingType,
    TaskImportance,
    TaskStatus,
    TreeScope,
)
from ..types_.outputs import (
    CustomField,
    Metadata,
    TaskDates,
    TaskEffort,
)
from ..types_.scalar import (
    AccountId,
    ContactId,
    CustomStatusId,
    DependencyId,
    FolderId,
    TaskId,
)


class Task(BaseEntity):
    id: TaskId
    account_id: AccountId
    title: str
    description: Optional[str]
    brief_description: Optional[str]
    parent_ids: Optional[Sequence[FolderId]]
    super_parent_ids: Optional[Sequence[FolderId]]
    shared_ids: Optional[Sequence[ContactId]]
    responsible_ids: Optional[Sequence[ContactId]]
    status: TaskStatus
    importance: TaskImportance
    created_date: datetime
    updated_date: datetime
    completed_date: Optional[datetime]
    dates: TaskDates
    scope: TreeScope
    author_ids: Optional[Sequence[ContactId]]
    custom_status_id: CustomStatusId
    has_attachments: Optional[bool]
    attachment_count: Optional[int]
    permalink: str
    priority: Optional[str]
    followed_by_me: Optional[bool]
    follower_ids: Optional[Sequence[ContactId]]
    recurrent: Optional[bool]
    super_task_ids: Optional[Sequence[TaskId]]
    sub_task_ids: Optional[Sequence[TaskId]]
    dependency_ids: Optional[Sequence[DependencyId]]
    metadata: Optional[Sequence[Metadata]]
    custom_fields: Optional[Sequence[CustomField]]
    billing_type: Optional[BillingType]
    effort_allocation: Optional[TaskEffort]
