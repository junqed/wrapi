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
from ..types_.inputs import DateRange
from ..types_.scalar import (
    CommentId,
    FolderId,
    TaskId,
)


class Comments(BaseEndpoint):
    plain_text: Optional[StrictBool]
    updated_date: Optional[DateRange]
    limit: Optional[int]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/comments",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.plain_text is not None:
            params["plainText"] = self._convert_bool(self.plain_text)

        if self.updated_date is not None:
            params["updatedDate"] = self._convert_input(self.updated_date)

        if self.limit is not None:
            params["limit"] = str(self.limit)

        return params


class _FilteredCommentsBaseEndpoint(BaseEndpoint):
    plain_text: Optional[StrictBool]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=self._url,
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.plain_text is not None:
            params["plainText"] = self._convert_bool(self.plain_text)

        return params

    @property
    def _url(self) -> str:
        raise NotImplementedError()


class CommentIds(_FilteredCommentsBaseEndpoint):
    comment_ids: Sequence[CommentId] = Field(..., max_length=100)

    @property
    def _url(self) -> str:
        return f"/comments/{','.join(self.comment_ids)}"


class FolderComments(_FilteredCommentsBaseEndpoint):
    folder_id: FolderId

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/comments"


class TaskComments(_FilteredCommentsBaseEndpoint):
    task_id: TaskId

    @property
    def _url(self) -> str:
        return f"/tasks/{self.task_id}/comments"


class _CreateOrModifyCommentBaseEndpoint(BaseEndpoint):
    text: str
    plain_text: Optional[StrictBool]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method=self._method,
            url=self._url,
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {"text": self.text}

        if self.plain_text is not None:
            body["plainText"] = self._convert_bool(self.plain_text)

        return body

    @property
    def _url(self) -> str:
        raise NotImplementedError()

    @property
    def _method(self) -> Methods:
        raise NotImplementedError()


class CreateFolderComment(_CreateOrModifyCommentBaseEndpoint):
    folder_id: FolderId

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/comments"

    @property
    def _method(self) -> Methods:
        return "POST"


class CreateTaskComment(_CreateOrModifyCommentBaseEndpoint):
    task_id: TaskId

    @property
    def _url(self) -> str:
        return f"/tasks/{self.task_id}/comments"

    @property
    def _method(self) -> Methods:
        return "POST"


class ModifyComment(_CreateOrModifyCommentBaseEndpoint):
    comment_id: CommentId

    @property
    def _url(self) -> str:
        return f"/comments/{self.comment_id}"

    @property
    def _method(self) -> Methods:
        return "PUT"


class DeleteComment(BaseEndpoint):
    comment_id: CommentId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/comments/{self.comment_id}",
        )
