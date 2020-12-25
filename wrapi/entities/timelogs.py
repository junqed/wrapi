from __future__ import annotations

from datetime import datetime
from typing import Optional

from ..types_.entity import BaseEntity
from ..types_.enums import BillingType
from ..types_.scalar import (
    ContactId,
    TaskId,
    TimelogCategoryId,
    TimelogId,
)


class Timelog(BaseEntity):
    id: TimelogId
    task_id: TaskId
    user_id: ContactId
    category_id: Optional[TimelogCategoryId]
    billing_type: Optional[BillingType]
    hours: int
    created_date: datetime
    updated_date: datetime
    tracked_date: datetime
    comment: str
