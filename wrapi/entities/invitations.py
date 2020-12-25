from __future__ import annotations

from datetime import datetime
from typing import Optional

from ..types_.entity import BaseEntity
from ..types_.enums import InvitationStatus, UserRole
from ..types_.scalar import (
    AccountId,
    ContactId,
    InvitationId,
)


class Invitation(BaseEntity):
    id: InvitationId
    account_id: AccountId
    first_name: Optional[str]
    last_name: Optional[str]
    email: str
    status: InvitationStatus
    inviter_user_id: ContactId
    invitation_date: datetime
    resolved_date: Optional[datetime]
    role: UserRole
    external: bool
