from __future__ import annotations

from ..api import EndpointData
from ..types_.endpoint import BaseEndpoint


class TimelogCategories(BaseEndpoint):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/timelog_categories",
        )
