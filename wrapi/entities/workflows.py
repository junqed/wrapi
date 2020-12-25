from __future__ import annotations

from typing import Sequence

from ..types_.entity import BaseEntity
from ..types_.outputs import WorkflowCustomField
from ..types_.scalar import WorkflowId


class Workflow(BaseEntity):
    id: WorkflowId
    name: str
    standard: bool
    hidden: bool
    custom_statuses: Sequence[WorkflowCustomField]
