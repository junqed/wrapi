from __future__ import annotations

from typing import Optional, Sequence

from pydantic.fields import Field
from pydantic.types import StrictBool

from ..api import (
    BodyParams,
    EndpointData,
    Methods,
    WrApiQueryParams,
)
from ..types_.endpoint import BaseEndpoint
from ..types_.inputs import (
    SpaceAccessType,
    SpaceMember,
    SpaceOptionalFields,
)
from ..types_.scalar import (
    AccessRoleId,
    ContactId,
    SpaceId,
)


class Spaces(BaseEndpoint):
    with_archived: Optional[StrictBool]
    user_is_member: Optional[StrictBool]
    fields_: Optional[Sequence[SpaceOptionalFields]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/spaces",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.with_archived is not None:
            params["withArchived"] = self._convert_bool(self.with_archived)

        if self.user_is_member is not None:
            params["userIsMember"] = self._convert_bool(self.user_is_member)

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class SpaceById(BaseEndpoint):
    space_id: SpaceId
    fields_: Optional[Sequence[SpaceOptionalFields]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/spaces/{self.space_id}",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class _CreateOrModifySpace(BaseEndpoint):
    description: Optional[str]
    guest_role_id: Optional[AccessRoleId]
    fields_: Optional[Sequence[SpaceOptionalFields]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method=self._method,
            url=self._url,
            body_params=self._body_params,
        )

    @property
    def _method(self) -> Methods:
        raise NotImplementedError()

    @property
    def _url(self) -> str:
        raise NotImplementedError()

    @property
    def _body_params(self) -> BodyParams:
        params: BodyParams = {}

        if self.description is not None:
            params["description"] = self.description

        if self.guest_role_id is not None:
            params["guestRoleId"] = self.guest_role_id

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class CreateSpace(_CreateOrModifySpace):
    access_type: SpaceAccessType
    title: str
    members: Optional[Sequence[SpaceMember]]

    @property
    def _method(self) -> Methods:
        return "POST"

    @property
    def _url(self) -> str:
        return "/spaces"

    @property
    def _body_params(self) -> BodyParams:
        params = {
            "accessType": self.access_type.value,
            "title": self.title,
        }

        if self.members:
            params["members"] = self._convert_input_seq(self.members)

        return {**super()._body_params, **params}


class ModifySpace(_CreateOrModifySpace):
    space_id: SpaceId
    access_type: Optional[SpaceAccessType]
    title: Optional[str]
    members_add: Optional[Sequence[SpaceMember]]
    members_update: Optional[Sequence[SpaceMember]]
    members_remove: Optional[Sequence[ContactId]]

    @property
    def _method(self) -> Methods:
        return "PUT"

    @property
    def _url(self) -> str:
        return f"/spaces/{self.space_id}"

    @property
    def _body_params(self) -> BodyParams:
        params = {}

        if self.access_type:
            params["accessType"] = self.access_type.value

        if self.title is not None:
            params["title"] = self.title

        if self.members_add:
            params["membersAdd"] = self._convert_input_seq(self.members_add)

        if self.members_update:
            params["membersUpdate"] = self._convert_input_seq(self.members_update)

        if self.members_remove:
            params["membersRemove"] = self._convert_seq(self.members_remove)

        return {**super()._body_params, **params}


class DeleteSpace(BaseEndpoint):
    space_id: SpaceId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/spaces/{self.space_id}",
        )
