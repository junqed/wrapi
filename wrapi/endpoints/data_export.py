from __future__ import annotations

from typing import Optional

from ..api import EndpointData, WrApiQueryParams
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import DataExportVersion
from ..types_.scalar import DataExportId


class DataExport(BaseEndpoint):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/data_export",
        )


class DataExportById(BaseEndpoint):
    data_export_id: DataExportId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/data_export/{self.data_export_id}",
        )


class RefreshDataExport(BaseEndpoint):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url="/data_export",
        )


class DataExportSchema(BaseEndpoint):
    version: Optional[DataExportVersion]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/data_export_schema",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.version is not None:
            params["version"] = self.version.value

        return params
