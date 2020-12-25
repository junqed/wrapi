from __future__ import annotations

from ..api import EndpointData
from ..types_.endpoint import BaseEndpoint
from ..types_.scalar import AsyncJobId


class AsyncJob(BaseEndpoint):
    async_job_id: AsyncJobId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/async_job/{self.async_job_id}",
        )
