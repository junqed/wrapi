from __future__ import annotations

from typing import Optional, Sequence

from ..types_.entity import BaseEntity
from ..types_.outputs import SpaceAccessType, SpaceMember
from ..types_.scalar import AccessRoleId, SpaceId


class Space(BaseEntity):
    id: SpaceId
    title: str
    description: str
    avatar_url: str
    access_type: SpaceAccessType
    archived: bool
    members: Optional[Sequence[SpaceMember]]
    guest_role_id: Optional[AccessRoleId]
