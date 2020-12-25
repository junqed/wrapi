from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic.fields import Field
from pydantic.types import StrictBool

from ..api import BodyParams, EndpointData
from ..types_.endpoint import BaseEndpoint
from ..types_.inputs import TaskReschedulingMode
from ..types_.scalar import FolderBluePrintId, FolderId


class FolderBlueprints(BaseEndpoint):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/folder_blueprints",
        )


class LaunchFolderBlueprint(BaseEndpoint):
    folder_blueprint_id: FolderBluePrintId

    parent: FolderId
    title: str
    title_prefix: Optional[str]
    copy_descriptions: Optional[StrictBool]
    notify_responsibles: Optional[StrictBool]
    copy_responsibles: Optional[StrictBool]
    copy_custom_fields: Optional[StrictBool]
    copy_attachments: Optional[StrictBool]
    reschedule_date: Optional[date]
    reschedule_mode: Optional[TaskReschedulingMode]
    entry_limit: Optional[int] = Field(None, ge=1, le=250)

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url=f"/folder_blueprints/{self.folder_blueprint_id}/launch_async",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {"parent": self.parent, "title": self.title}

        if self.title_prefix is not None:
            body["titlePrefix"] = self.title_prefix

        if self.copy_descriptions is not None:
            body["copyDescriptions"] = self._convert_bool(self.copy_descriptions)

        if self.notify_responsibles is not None:
            body["notifyResponsibles"] = self._convert_bool(self.notify_responsibles)

        if self.copy_responsibles is not None:
            body["copyResponsibles"] = self._convert_bool(self.copy_responsibles)

        if self.copy_custom_fields is not None:
            body["copyCustomFields"] = self._convert_bool(self.copy_custom_fields)

        if self.copy_attachments is not None:
            body["copyAttachments"] = self._convert_bool(self.copy_attachments)

        if self.reschedule_date:
            body["rescheduleDate"] = self.reschedule_date.isoformat()

        if self.reschedule_mode:
            body["rescheduleMode"] = self.reschedule_mode.value

        if self.entry_limit is not None:
            body["entryLimit"] = str(self.entry_limit)

        return body
