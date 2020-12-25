from __future__ import annotations

from typing import Optional, Sequence

from pydantic.fields import Field
from pydantic.types import StrictBool

from ..api import EndpointData, WrApiQueryParams
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import Size
from ..types_.inputs import DateRange
from ..types_.scalar import (
    AttachmentId,
    FolderId,
    TaskId,
)


class _BaseAttachments(BaseEndpoint):
    versions: Optional[StrictBool]
    created_date: Optional[DateRange]
    with_urls: Optional[StrictBool]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=self._url,
            query_params=self._query_params,
        )

    @property
    def _url(self) -> str:
        raise NotImplementedError()

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.versions is not None:
            params["versions"] = self._convert_bool(self.versions)

        if self.created_date is not None:
            params["createdDate"] = self._convert_input(self.created_date)

        if self.with_urls is not None:
            params["withUrls"] = self._convert_bool(self.with_urls)

        return params


class Attachments(BaseEndpoint):
    @property
    def _url(self) -> str:
        return "/attachments"


class FolderAttachments(BaseEndpoint):
    folder_id: FolderId

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/attachments"


class TaskAttachments(BaseEndpoint):
    task_id: TaskId

    @property
    def _url(self) -> str:
        return f"/tasks/{self.task_id}/attachments"


class AttachmentsById(BaseEndpoint):
    task_ids: Sequence[TaskId] = Field(..., max_length=100)
    versions: Optional[StrictBool]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/attachments/{','.join(self.task_ids)}",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.versions is not None:
            params["versions"] = self._convert_bool(self.versions)

        return params


class DownloadAttachment(BaseEndpoint):
    attachment_id: AttachmentId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/attachments/{self.attachment_id}/download",
        )


class DownloadPreviewAttachment(BaseEndpoint):
    attachment_id: AttachmentId
    size: Optional[Size]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/attachments/{self.attachment_id}/preview",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.size is not None:
            params["size"] = self.size.value

        return params


class AccessUrlAttachment(BaseEndpoint):
    attachment_id: AttachmentId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/attachments/{self.attachment_id}/url",
        )
