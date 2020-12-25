from __future__ import annotations

from typing import Optional, Sequence

from ..api import BodyParams, EndpointData
from ..types_.endpoint import BaseEndpoint
from ..types_.inputs import EDiscoverySearchScope
from ..types_.scalar import ContactId


class EDiscoverySearch(BaseEndpoint):
    scopes: Sequence[EDiscoverySearchScope]
    terms: Optional[Sequence[str]]
    target_user_id: Optional[ContactId]
    timeout: Optional[int]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url="/ediscovery_search",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {
            "scopes": self._convert_seq(self.scopes),
        }

        if self.terms:
            body["terms"] = self._convert_seq(self.terms)

        if self.target_user_id:
            body["targetUserId"] = self.target_user_id

        if self.timeout is not None:
            body["timeout"] = str(self.timeout)

        return body
