from __future__ import annotations

from typing import Optional

from pydantic.fields import Field
from pydantic.types import StrictBool

from ..api import BodyParams, EndpointData
from ..types_.endpoint import BaseEndpoint
from ..types_.inputs import WorkflowCustomField
from ..types_.scalar import WorkflowId


class Workflows(BaseEndpoint):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/workflows",
        )


class CreateWorkflow(BaseEndpoint):
    name: str = Field(..., max_length=128)

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(method="POST", url="/workflows", body_params=self._body_params)

    @property
    def _body_params(self) -> BodyParams:
        return {"name": self.name}


class ModifyWorkflow(BaseEndpoint):
    workflow_id: WorkflowId
    name: Optional[str] = Field(..., max_length=128)
    hidden: Optional[StrictBool]
    custom_status: Optional[WorkflowCustomField]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(method="PUT", url=f"/workflows/{self.workflow_id}", body_params=self._body_params)

    @property
    def _body_params(self) -> BodyParams:
        body = {}

        if self.name is not None:
            body["name"] = self.name

        if self.hidden is not None:
            body["hidden"] = self._convert_bool(self.hidden)

        if self.custom_status:
            body["custom_status"] = self._convert_input(self.custom_status)

        return body
