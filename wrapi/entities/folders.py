from __future__ import annotations

from datetime import datetime
from typing import Optional, Sequence

from ..types_.entity import BaseEntity
from ..types_.enums import Color, TreeScope
from ..types_.outputs import (
    CustomField,
    Metadata,
    Project,
)
from ..types_.scalar import (
    AccountId,
    ContactId,
    CustomFieldId,
    FolderId,
    WorkflowId,
)


class _BaseFolder(BaseEntity):
    id: FolderId
    title: str
    color: Optional[Color]
    child_ids: Optional[Sequence[FolderId]]
    scope: TreeScope
    project: Optional[Project]


class FolderTree(_BaseFolder):
    space: bool


class Folder(_BaseFolder):
    account_id: AccountId
    created_date: datetime
    updated_date: datetime
    brief_description: Optional[str]
    description: Optional[str]
    shared_ids: Sequence[ContactId]
    parent_ids: Sequence[ContactId]
    super_parent_ids: Optional[Sequence[FolderId]]
    has_attachments: Optional[bool]
    attachment_count: Optional[int]
    permalink: str
    workflow_id: WorkflowId
    metadata: Optional[Sequence[Metadata]]
    custom_fields: Optional[Sequence[CustomField]]
    custom_column_ids: Optional[Sequence[CustomFieldId]]
