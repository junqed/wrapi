from __future__ import annotations

from typing import (
    Literal,
    Optional,
    Sequence,
)

from pydantic.fields import Field

from ..api import (
    BodyParams,
    EndpointData,
    WrApiQueryParams,
)
from ..types_.endpoint import BaseEndpoint
from ..types_.inputs import (
    Avatar,
    ContactsOptionalFields,
    GroupUpdate,
    Metadata,
)
from ..types_.scalar import ContactId, GroupId


class GroupById(BaseEndpoint):
    group_id: GroupId
    fields_: Optional[Sequence[Literal[ContactsOptionalFields.METADATA]]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/groups/{self.group_id}",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class Groups(BaseEndpoint):
    page_size: Optional[int]
    page_token: Optional[str]
    metadata: Optional[Metadata]
    fields_: Optional[Sequence[Literal[ContactsOptionalFields.METADATA]]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/groups",
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


class CreateGroup(BaseEndpoint):
    title: str
    members: Optional[Sequence[ContactId]]
    parent: Optional[ContactId]
    avatar: Optional[Avatar]
    metadata: Optional[Sequence[Metadata]]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url="/groups",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {"title": self.title}

        if self.members is not None:
            body["members"] = self._convert_seq(self.members)

        if self.parent:
            body["parent"] = self.parent

        if self.avatar is not None:
            body["avatar"] = self._convert_input(self.avatar)

        if self.metadata:
            body["metadata"] = self._convert_input_seq(self.metadata)

        return body


class BulkModifyGroup(BaseEndpoint):
    members: Sequence[GroupUpdate]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url="/groups_bulk",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        return {"members": self._convert_input_seq(self.members)}


class ModifyGroup(CreateGroup):
    group_id: GroupId
    add_members: Optional[Sequence[ContactId]]
    remove_members: Optional[Sequence[ContactId]]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url=f"/groups/{self.group_id}",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = super()._body_params

        if self.add_members is not None:
            body["addMembers"] = self._convert_seq(self.add_members)

        if self.remove_members is not None:
            body["removeMembers"] = self._convert_seq(self.remove_members)

        return body


class DeleteGroup(BaseEndpoint):
    group_id: GroupId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/groups/{self.group_id}",
        )
