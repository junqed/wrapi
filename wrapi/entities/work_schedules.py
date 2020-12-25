from __future__ import annotations

from typing import Optional, Sequence

from pydantic.types import Json

from ..types_.entity import BaseEntity
from ..types_.outputs import WorkScheduleType
from ..types_.scalar import ContactId, WorkScheduleId


class WorkSchedule(BaseEntity):
    id: WorkScheduleId
    schedule_type: WorkScheduleType
    title: str
    workweek: Optional[Sequence[Json]]
    user_ids: Sequence[ContactId]
