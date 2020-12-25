from __future__ import annotations

from datetime import datetime
from typing import (
    Literal,
    Optional,
    Sequence,
    Union,
)

from ..types_.entity import BaseEntity
from ..types_.enums import WeekDay
from ..types_.outputs import Metadata, Subscription
from ..types_.scalar import AccountId, FolderId
from .custom_fields import CustomField


class Account(BaseEntity):
    id: AccountId
    name: str
    date_format: Union[Literal["dd/MM/yyyy"], Literal["MM/dd/yyyy"]]
    first_day_of_week: Union[Literal[WeekDay.SAT], Literal[WeekDay.SUN], Literal[WeekDay.MON]]
    work_days: Sequence[WeekDay]
    root_folder_id: FolderId
    recycle_bin_id: FolderId
    created_date: datetime
    subscription: Optional[Subscription]
    metadata: Optional[Metadata]
    custom_fields: Optional[Sequence[CustomField]]
    joined_date: datetime
