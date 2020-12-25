from __future__ import annotations

from typing import Optional

from pydantic.types import StrictBool

from ..api import BodyParams, EndpointData
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import UserRole
from ..types_.scalar import InvitationId


class Invitations(BaseEndpoint):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/invitations",
        )


class CreateInvitation(BaseEndpoint):
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    role: Optional[UserRole]
    external: Optional[StrictBool]
    subject: Optional[str]
    message: Optional[str]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url="/invitations",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {"email": self.email}

        if self.first_name is not None:
            body["firstName"] = self.first_name

        if self.last_name is not None:
            body["lastName"] = self.last_name

        if self.role:
            body["role"] = self.role.value

        if self.external is not None:
            body["external"] = self._convert_bool(self.external)

        if self.subject is not None:
            body["subject"] = self.subject

        if self.message is not None:
            body["message"] = self.message

        return body


class ModifyInvitation(BaseEndpoint):
    invitation_id: InvitationId
    resend: Optional[StrictBool]
    role: Optional[UserRole]
    external: Optional[StrictBool]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url=f"/invitations/{self.invitation_id}",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {}

        if self.resend is not None:
            body["resend"] = self._convert_bool(self.resend)

        if self.role:
            body["role"] = self.role.value

        if self.external is not None:
            body["external"] = self._convert_bool(self.external)

        return body


class DeleteInvitation(BaseEndpoint):
    invitation_id: InvitationId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/invitations/{self.invitation_id}",
        )
