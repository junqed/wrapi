from __future__ import annotations

from typing import Optional, Sequence

from ..types_.entity import BaseEntity
from ..types_.outputs import Metadata
from ..types_.scalar import AccountId, ContactId


class Group(BaseEntity):
    id: ContactId
    account_id: AccountId
    title: str
    member_ids: Sequence[ContactId]
    child_ids: Sequence[ContactId]
    parent_ids: Sequence[ContactId]
    avatar_url: str
    my_team: Optional[bool]
    metadata: Optional[Metadata]
