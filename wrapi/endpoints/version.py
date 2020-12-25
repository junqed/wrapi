from __future__ import annotations

from ..api import EndpointData
from ..types_.endpoint import BaseEndpoint


class Version(BaseEndpoint):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/version",
        )
