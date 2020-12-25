from __future__ import annotations

from typing import Optional, Sequence

from ..types_.entity import BaseEntity
from ..types_.outputs import (
    Metadata,
    UserRole,
    UserType,
)
from ..types_.scalar import (
    AccountId,
    ContactId,
    WorkScheduleId,
)


class Profile(BaseEntity):
    account_id: AccountId
    email: str
    role: UserRole
    external: bool
    admin: bool
    owner: bool


class Contact(BaseEntity):
    id: ContactId
    first_name: str
    last_name: str
    type: UserType
    avatar_url: str
    timezone: str
    locale: str
    deleted: bool
    profiles: Sequence[Profile]
    me: Optional[bool]
    member_ids: Optional[Sequence[ContactId]]
    metadata: Optional[Sequence[Metadata]]
    my_team: Optional[bool]
    title: Optional[str]
    company_name: Optional[str]
    phone: Optional[str]
    location: Optional[str]
    work_schedule_id: Optional[WorkScheduleId]
