from __future__ import annotations

from typing import Optional, Sequence

from pydantic.fields import Field

from ..api import BodyParams, EndpointData
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import CustomFieldType
from ..types_.inputs import CustomFieldSettings
from ..types_.scalar import ContactId, CustomFieldId


class CustomFields(BaseEndpoint):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/customfields",
        )


class CustomFieldsByIds(BaseEndpoint):
    custom_field_ids: Sequence[CustomFieldId] = Field(..., max_length=100)

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/customfields/{','.join(self.custom_field_ids)}",
        )


class CreateCustomField(BaseEndpoint):
    title: str
    type: CustomFieldType
    shareds: Optional[Sequence[ContactId]]
    settings: Optional[CustomFieldSettings]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url="/customfields",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {"title": self.title, "type": self.type.value}

        if self.settings:
            body["settings"] = self._convert_input(self.settings)

        if self.shareds is not None:
            body["shareds"] = self._convert_seq(self.shareds)

        return body


class ModifyCustomField(BaseEndpoint):
    custom_field_id: CustomFieldId
    title: Optional[str]
    type: Optional[CustomFieldType]
    add_shareds: Optional[Sequence[ContactId]]
    remove_shareds: Optional[Sequence[ContactId]]
    settings: Optional[CustomFieldSettings]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url=f"/customfields/{self.custom_field_id}",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {}

        if self.title is not None:
            body["title"] = self.title

        if self.type:
            body["type"] = self.type.value

        if self.add_shareds is not None:
            body["addShareds"] = self._convert_seq(self.add_shareds)

        if self.remove_shareds is not None:
            body["removeShareds"] = self._convert_seq(self.remove_shareds)

        if self.settings:
            body["settings"] = self._convert_input(self.settings)

        return body
