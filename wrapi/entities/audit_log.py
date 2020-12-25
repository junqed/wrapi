from __future__ import annotations

from datetime import datetime

from pydantic.types import Json

from ..types_.entity import BaseEntity
from ..types_.enums import AuditLogOperation
from ..types_.outputs import AuditObjectType
from ..types_.scalar import AuditLogId, ContactId


class AuditLog(BaseEntity):
    id: AuditLogId
    operation: AuditLogOperation
    user_id: ContactId
    user_email: str
    event_date: datetime
    ip_address: str
    object_type: AuditObjectType
    object_name: str
    object_id: str
    details: Json
