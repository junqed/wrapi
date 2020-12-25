from __future__ import annotations

from typing import Optional, Sequence

from ..api import EndpointData, WrApiQueryParams
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import AuditLogOperation
from ..types_.inputs import DateRange


class AuditLog(BaseEndpoint):
    event_date: Optional[DateRange]
    operations: Optional[Sequence[AuditLogOperation]]
    page_size: Optional[int]
    next_page_token: Optional[str]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/audit_log",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.event_date:
            params["eventDate"] = self._convert_input(self.event_date)

        if self.operations:
            params["operations"] = self._convert_seq(self.operations)

        if self.page_size is not None:
            params["pageSize"] = str(self.page_size)

        if self.next_page_token:
            params["nextPageToken"] = self.next_page_token

        return params
