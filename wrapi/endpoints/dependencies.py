from __future__ import annotations

from typing import Sequence

from pydantic.fields import Field

from ..api import BodyParams, EndpointData
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import DependencyRelationType
from ..types_.scalar import DependencyId, TaskId


class TaskDependencies(BaseEndpoint):
    task_id: TaskId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/tasks/{self.task_id}/dependencies",
        )


class DependenciesById(BaseEndpoint):
    dependency_ids: Sequence[DependencyId] = Field(..., max_length=100)

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/dependencies/{','.join(self.dependency_ids)}",
        )


class CreateDependency(BaseEndpoint):
    task_id: TaskId
    predecessor_id: TaskId
    successor_id: TaskId
    relationType: DependencyRelationType

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url=f"/tasks/{self.task_id}/dependencies",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        return {
            "predecessorId": self.predecessor_id,
            "successorId": self.successor_id,
            "relationType": self.relationType.value,
        }


class ModifyDependency(BaseEndpoint):
    dependency_id: TaskId
    relationType: DependencyRelationType

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url=f"/dependencies/{self.dependency_id}",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        return {
            "relationType": self.relationType.value,
        }


class DeleteDependency(BaseEndpoint):
    dependency_id: TaskId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/dependencies/{self.dependency_id}",
        )
