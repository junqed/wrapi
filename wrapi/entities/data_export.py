from __future__ import annotations

from datetime import datetime
from typing import Optional, Sequence

from pydantic.types import Json

from ..types_.entity import BaseEntity
from ..types_.enums import ColumnDataType, DataExportStatus
from ..types_.outputs import DataExportResource
from ..types_.scalar import DataExportId


class DataExport(BaseEntity):
    id: DataExportId
    completed_date: Optional[datetime]
    status: DataExportStatus
    resources: Optional[Sequence[DataExportResource]]


class DataExportResourceColumn(BaseEntity):
    id: str
    alias: str
    data_type: ColumnDataType
    foreign_key: Optional[Json]


class DataExportSchema(BaseEntity):
    id: str
    alias: str
    columns: Sequence[DataExportResourceColumn]
