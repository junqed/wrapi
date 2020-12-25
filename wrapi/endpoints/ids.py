from __future__ import annotations

from typing import Sequence

from ..api import EndpointData, WrApiQueryParams
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import V2EntityType


class Ids(BaseEndpoint):
    type: V2EntityType
    ids: Sequence[int]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/ids",
            query_params=self.query_params,
        )

    @property
    def query_params(self) -> WrApiQueryParams:
        return WrApiQueryParams(type=self.type.value, ids=self._convert_seq(self.ids))
