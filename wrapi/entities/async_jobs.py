from __future__ import annotations

from typing import Optional

from pydantic.types import Json

from ..types_.entity import BaseEntity
from ..types_.outputs import AsyncJobStatus, AsyncJobType
from ..types_.scalar import AsyncJobId


class AsyncJob(BaseEntity):
    id: AsyncJobId
    status: AsyncJobStatus
    progress_percent: int
    total_count: Optional[int]
    processed_count: Optional[int]
    type: AsyncJobType
    result: Optional[Json]
    error_message: Optional[str]
