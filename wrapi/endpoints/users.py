from __future__ import annotations

from ..api import EndpointData, WrApiQueryParams
from ..types_.endpoint import BaseEndpoint
from ..types_.inputs import Profile
from ..types_.scalar import ContactId


class Users(BaseEndpoint):
    user_id: ContactId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/users/{self.user_id}",
        )


class ModifyUser(BaseEndpoint):
    user_id: ContactId
    profile: Profile

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url=f"/users/{self.user_id}",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        return WrApiQueryParams({"profile": self._convert_input(self.profile)})
