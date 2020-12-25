from __future__ import annotations

from datetime import date
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
from ..types_.inputs import ApprovalFinalStatus, DateRange
from ..types_.scalar import (
    ApprovalId,
    AttachmentId,
    ContactId,
    FolderId,
    TaskId,
)


class Approvals(BaseEndpoint):
    statuses: Optional[ApprovalFinalStatus]
    updated_date: Optional[DateRange]
    approvers: Optional[Sequence[ContactId]]
    pending_approvers: Optional[Sequence[ContactId]]
    limit: Optional[int]
    page_size: Optional[int]
    next_page_token: Optional[str]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/approvals",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.statuses is not None:
            params["statuses"] = self.statuses.value

        if self.updated_date is not None:
            params["updatedDate"] = self._convert_input(self.updated_date)

        if self.approvers:
            params["approvers"] = self._convert_seq(self.approvers)

        if self.pending_approvers:
            params["pendingApprovers"] = self._convert_seq(self.pending_approvers)

        if self.limit is not None:
            params["limit"] = str(self.limit)

        if self.page_size is not None:
            params["pageSize"] = str(self.page_size)

        if self.next_page_token:
            params["nextPageToken"] = self.next_page_token

        return params


class _FilteredApprovalsBaseEndpoint(BaseEndpoint):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=self._url,
        )

    @property
    def _url(self) -> str:
        raise NotImplementedError()


class FolderApprovals(_FilteredApprovalsBaseEndpoint):
    folder_id: FolderId

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/approvals"


class TaskApprovals(_FilteredApprovalsBaseEndpoint):
    task_id: TaskId

    @property
    def _url(self) -> str:
        return f"/tasks/{self.task_id}/approvals"


class ApprovalsByIds(_FilteredApprovalsBaseEndpoint):
    approval_ids: Sequence[ApprovalId] = Field(..., max_length=100)

    @property
    def _url(self) -> str:
        return f"/approvals/{','.join(self.approval_ids)}"


class _CreateOrModifyApprovalBaseEndpoint(BaseEndpoint):
    description: Optional[str]
    due_date: Optional[date]
    auto_finish_on_approve: Optional[StrictBool]  # bool but str in the docs
    auto_finish_on_reject: Optional[StrictBool]  # bool but str in the docs

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method=self._method,
            url=self._url,
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {}

        if self.description is not None:
            body["description"] = self.description

        if self.due_date:
            body["dueDate"] = self.due_date.isoformat()

        if self.auto_finish_on_approve is not None:
            body["autoFinishOnApprove"] = self._convert_bool(self.auto_finish_on_approve)

        if self.auto_finish_on_reject is not None:
            body["autoFinishOnReject"] = self._convert_bool(self.auto_finish_on_reject)

        return body

    @property
    def _url(self) -> str:
        raise NotImplementedError()

    @property
    def _method(self) -> Methods:
        raise NotImplementedError()


class _CreateApprovalBaseEndpoint(_CreateOrModifyApprovalBaseEndpoint):
    approvers: Optional[Sequence[ContactId]]
    attachments: Optional[Sequence[AttachmentId]]

    @property
    def _body_params(self) -> BodyParams:
        body = super()._body_params

        if self.approvers:
            body["approvers"] = self._convert_seq(self.approvers)

        if self.attachments:
            body["attachments"] = self._convert_seq(self.attachments)

        return body


class CreateFolderApproval(_CreateApprovalBaseEndpoint):
    folder_id: FolderId

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/approvals"

    @property
    def _method(self) -> Methods:
        return "POST"


class CreateTaskApproval(_CreateApprovalBaseEndpoint):
    task_id: TaskId

    @property
    def _url(self) -> str:
        return f"/tasks/{self.task_id}/approvals"

    @property
    def _method(self) -> Methods:
        return "POST"


class ModifyApproval(_CreateOrModifyApprovalBaseEndpoint):
    approval_id: ApprovalId
    add_approvers: Optional[Sequence[ContactId]]
    remove_approvers: Optional[Sequence[ContactId]]
    add_attachments: Optional[Sequence[AttachmentId]]
    remove_attachments: Optional[Sequence[AttachmentId]]

    @property
    def _url(self) -> str:
        return f"/approvals/{self.approval_id}"

    @property
    def _method(self) -> Methods:
        return "PUT"

    @property
    def _body_params(self) -> BodyParams:
        body = super()._body_params

        if self.add_approvers:
            body["addApprovers"] = self._convert_seq(self.add_approvers)

        if self.remove_approvers:
            body["removeApprovers"] = self._convert_seq(self.remove_approvers)

        if self.add_attachments:
            body["addAttachments"] = self._convert_seq(self.add_attachments)

        if self.remove_attachments:
            body["removeAttachments"] = self._convert_seq(self.remove_attachments)

        return body


class DeleteApproval(BaseEndpoint):
    approval_id: ApprovalId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/approvals/{self.approval_id}",
        )
