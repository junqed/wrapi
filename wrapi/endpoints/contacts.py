from __future__ import annotations

from typing import Optional, Sequence

from pydantic.fields import Field
from pydantic.types import StrictBool

from ..api import EndpointData, WrApiQueryParams
from ..types_.endpoint import BaseEndpoint
from ..types_.inputs import ContactsOptionalFields, Metadata
from ..types_.scalar import ContactId


class Contacts(BaseEndpoint):
    me: Optional[StrictBool]
    metadata: Optional[Metadata]
    deleted: Optional[StrictBool]
    fields_: Optional[Sequence[ContactsOptionalFields]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/contacts",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.metadata:
            params["metadata"] = self._convert_input(self.metadata)

        if self.me is not None:
            params["me"] = self._convert_bool(self.me)

        if self.deleted is not None:
            params["deleted"] = self._convert_bool(self.deleted)

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class ContactsIds(BaseEndpoint):
    contact_ids: Sequence[ContactId]
    metadata: Optional[Metadata]
    fields_: Optional[Sequence[ContactsOptionalFields]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/contacts/{','.join(self.contact_ids)}",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.metadata:
            params["metadata"] = self._convert_input(self.metadata)

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class ModifyContact(BaseEndpoint):
    contact_id: ContactId
    metadata: Optional[Metadata]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url=f"/contacts/{self.contact_id}",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.metadata:
            params["metadata"] = self._convert_input(self.metadata)

        return params
