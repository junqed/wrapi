from __future__ import annotations

from ..types_.entity import BaseEntity
from ..types_.scalar import AccessRoleId


class AccessRole(BaseEntity):
    id: AccessRoleId
    title: str
    description: str
