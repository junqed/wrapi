from __future__ import annotations

from typing import Optional, Sequence

from pydantic.fields import Field

from ..api import (
    BodyParams,
    EndpointData,
    WrApiQueryParams,
)
from ..types_.endpoint import BaseEndpoint
from ..types_.inputs import AccountOptionalFields, Metadata


class Account(BaseEndpoint):
    metadata: Optional[Metadata]
    fields_: Optional[Sequence[AccountOptionalFields]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/account",
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


class ModifyAccount(BaseEndpoint):
    metadata: Optional[Sequence[Metadata]]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url="/account",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {}

        if self.metadata:
            body["metadata"] = self._convert_input_seq(self.metadata)

        return body
