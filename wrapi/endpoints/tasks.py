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
from ..types_.enums import (
    BillingType,
    TaskImportance,
    TaskSortFilter,
    TaskSortOrder,
    TaskStatus,
    TaskType,
)
from ..types_.inputs import (
    CustomField,
    CustomFieldFilter,
    Metadata,
    ShortTaskOptionalFields,
    TaskDateRangeEqualFilter,
    TaskDates,
    TaskDatetimeRangeEqualFilter,
    TaskDatetimeRangeFilter,
    TaskEffort,
    TaskOptionalFields,
)
from ..types_.scalar import (
    ContactId,
    CustomStatusId,
    FolderId,
    SpaceId,
    TaskId,
)


class _BaseTasks(BaseEndpoint):
    descendants: Optional[StrictBool]
    title: Optional[str]
    status: Optional[TaskStatus]
    importance: Optional[TaskImportance]
    start_date: Optional[TaskDatetimeRangeEqualFilter]
    due_date: Optional[TaskDatetimeRangeEqualFilter]
    scheduled_date: Optional[TaskDateRangeEqualFilter]
    created_date: Optional[TaskDatetimeRangeFilter]
    updated_date: Optional[TaskDatetimeRangeFilter]
    completed_date: Optional[TaskDatetimeRangeFilter]
    authors: Optional[Sequence[str]]
    responsibles: Optional[Sequence[str]]
    permalink: Optional[str]
    type: Optional[TaskType]
    limit: Optional[int]
    sort_field: Optional[TaskSortFilter]
    sort_order: Optional[TaskSortOrder]
    sub_tasks: Optional[StrictBool]
    page_size: Optional[int]
    next_page_token: Optional[str]
    metadata: Optional[Metadata]
    custom_field: Optional[CustomFieldFilter]
    custom_statuses: Optional[Sequence[str]]
    billing_types: Optional[Sequence[BillingType]]
    fields_: Optional[Sequence[TaskOptionalFields]] = Field(None, alias="fields")

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

        if self.descendants is not None:
            params["descendants"] = self._convert_bool(self.descendants)

        if self.title:
            params["title"] = self.title

        if self.status:
            params["status"] = self.status.value

        if self.importance:
            params["importance"] = self.importance.value

        if self.start_date:
            params["startDate"] = self._convert_input(self.start_date)

        if self.due_date:
            params["dueDate"] = self._convert_input(self.due_date)

        if self.scheduled_date:
            params["scheduledDate"] = self._convert_input(self.scheduled_date)

        if self.created_date:
            params["createdDate"] = self._convert_input(self.created_date)

        if self.updated_date:
            params["updatedDate"] = self._convert_input(self.updated_date)

        if self.completed_date:
            params["completedDate"] = self._convert_input(self.completed_date)

        if self.authors:
            params["authors"] = self._convert_seq(self.authors)

        if self.responsibles:
            params["responsibles"] = self._convert_seq(self.responsibles)

        if self.permalink:
            params["permalink"] = self.permalink

        if self.type:
            params["type"] = self.type.value

        if self.limit is not None:
            params["limit"] = str(self.limit)

        if self.sort_field:
            params["sortField"] = self.sort_field.value

        if self.sort_order:
            params["sortOrder"] = self.sort_order.value

        if self.sub_tasks is not None:
            params["subTasks"] = self._convert_bool(self.sub_tasks)

        if self.page_size is not None:
            params["pageSize"] = str(self.page_size)

        if self.next_page_token:
            params["nextPageToken"] = self.next_page_token

        if self.metadata:
            params["metadata"] = self._convert_input(self.metadata)

        if self.custom_field:
            params["customField"] = self._convert_input(self.custom_field)

        if self.custom_statuses:
            params["customStatuses"] = self._convert_seq(self.custom_statuses)

        if self.billing_types:
            params["billingTypes"] = self._convert_seq(self.billing_types)

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class Tasks(_BaseTasks):
    @property
    def _url(self) -> str:
        return "/tasks"


class TasksInFolder(_BaseTasks):
    folder_id: FolderId

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/tasks"


class TasksInSpace(_BaseTasks):
    space_id: SpaceId

    @property
    def _url(self) -> str:
        return f"/spaces/{self.space_id}/tasks"


class TasksById(_BaseTasks):
    task_ids: Sequence[TaskId] = Field(..., max_length=100)

    @property
    def _url(self) -> str:
        return f"/tasks/{','.join(self.task_ids)}"


class _CreateOrModifyTask(BaseEndpoint):
    description: Optional[str]
    status: Optional[TaskStatus]
    importance: Optional[TaskImportance]
    dates: Optional[TaskDates]
    follow: Optional[StrictBool]
    priority_before: Optional[TaskId]
    priority_after: Optional[TaskId]
    metadata: Optional[Sequence[Metadata]]
    custom_fields: Optional[Sequence[CustomField]]
    custom_status: Optional[CustomStatusId]
    effort_allocation: Optional[TaskEffort]
    billing_type: Optional[BillingType]
    fields_: Optional[Sequence[ShortTaskOptionalFields]] = Field(None, alias="fields")

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

        if self.status:
            params["status"] = self.status.value

        if self.importance:
            params["importance"] = self.importance.value

        if self.dates:
            params["dates"] = self._convert_input(self.dates)

        if self.follow is not None:
            params["follow"] = self._convert_bool(self.follow)

        if self.priority_before is not None:
            params["priorityBefore"] = self.priority_before

        if self.priority_after is not None:
            params["priorityAfter"] = self.priority_after

        if self.metadata:
            params["metadata"] = self._convert_input_seq(self.metadata)

        if self.custom_fields:
            params["customFields"] = self._convert_input_seq(self.custom_fields)

        if self.custom_status is not None:
            params["customStatus"] = self.custom_status

        if self.effort_allocation:
            params["effortAllocation"] = self._convert_input(self.effort_allocation)

        if self.billing_type:
            params["billingType"] = self.billing_type.value

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class CreateTask(_CreateOrModifyTask):
    folder_id: FolderId
    title: str
    shareds: Optional[Sequence[ContactId]]
    parents: Optional[Sequence[FolderId]]
    responsibles: Optional[Sequence[ContactId]]
    followers: Optional[Sequence[ContactId]]
    super_tasks: Optional[Sequence[TaskId]]

    @property
    def _method(self) -> Methods:
        return "POST"

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/tasks"

    @property
    def _body_params(self) -> BodyParams:
        params = super()._body_params
        params["title"] = self.title

        if self.shareds is not None:
            params["shared"] = self._convert_seq(self.shareds)

        if self.parents is not None:
            params["parents"] = self._convert_seq(self.parents)

        if self.followers is not None:
            params["followers"] = self._convert_seq(self.followers)

        if self.responsibles is not None:
            params["responsibles"] = self._convert_seq(self.responsibles)

        if self.super_tasks is not None:
            params["superTasks"] = self._convert_seq(self.super_tasks)

        return params


class ModifyTask(_CreateOrModifyTask):
    task_id: TaskId
    title: Optional[str]
    add_parents: Optional[Sequence[FolderId]]
    remove_parents: Optional[Sequence[FolderId]]
    add_shareds: Optional[Sequence[ContactId]]
    remove_shareds: Optional[Sequence[ContactId]]
    add_responsibles: Optional[Sequence[ContactId]]
    remove_responsibles: Optional[Sequence[ContactId]]
    add_followers: Optional[Sequence[ContactId]]
    add_super_tasks: Optional[Sequence[TaskId]]
    remove_super_tasks: Optional[Sequence[TaskId]]
    restore: Optional[StrictBool]

    @property
    def _method(self) -> Methods:
        return "PUT"

    @property
    def _url(self) -> str:
        return f"/tasks/{self.task_id}"

    @property
    def _body_params(self) -> BodyParams:
        params = super()._body_params

        if self.title is not None:
            params["title"] = self.title

        if self.add_parents is not None:
            params["addParents"] = self._convert_seq(self.add_parents)

        if self.remove_parents is not None:
            params["removeParents"] = self._convert_seq(self.remove_parents)

        if self.add_responsibles is not None:
            params["addResponsibles"] = self._convert_seq(self.add_responsibles)

        if self.remove_responsibles is not None:
            params["removeResponsibles"] = self._convert_seq(self.remove_responsibles)

        if self.add_followers is not None:
            params["addFollowers"] = self._convert_seq(self.add_followers)

        if self.add_super_tasks is not None:
            params["addSuperTasks"] = self._convert_seq(self.add_super_tasks)

        if self.remove_super_tasks is not None:
            params["removeSuperTasks"] = self._convert_seq(self.remove_super_tasks)

        if self.restore is not None:
            params["restore"] = self._convert_bool(self.restore)

        return params


class ModifyTasksById(BaseEndpoint):
    task_ids: Sequence[TaskId] = Field(..., max_length=100)
    custom_fields: Optional[Sequence[CustomField]]
    effort_allocation: Optional[TaskEffort]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url=f"/tasks/{','.join(self.task_ids)}",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        params = {}

        if self.custom_fields is not None:
            params["customFields"] = self._convert_input_seq(self.custom_fields)

        if self.effort_allocation:
            params["effortAllocation"] = self._convert_input(self.effort_allocation)

        return params


class DeleteTask(BaseEndpoint):
    task_id: TaskId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/tasks/{self.task_id}",
        )
