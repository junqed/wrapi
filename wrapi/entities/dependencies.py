from __future__ import annotations

from ..types_.entity import BaseEntity
from ..types_.enums import DependencyRelationType
from ..types_.scalar import DependencyId, TaskId


class Dependency(BaseEntity):
    id: DependencyId
    predecessor_id: TaskId
    successor_id: TaskId
    relation_type: DependencyRelationType
