from __future__ import annotations

from datetime import date
from typing import (
    Literal,
    Optional,
    Sequence,
)

from pydantic.fields import Field
from pydantic.types import StrictBool

from ..api import (
    BodyParams,
    EndpointData,
    Methods,
    WrApiQueryParams,
)
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import BillingType
from ..types_.inputs import DateRange, TimelogOptionalFields
from ..types_.scalar import (
    ContactId,
    FolderId,
    TaskId,
    TimelogCategoryId,
    TimelogId,
)


class _BaseTimelogs(BaseEndpoint):
    created_date: Optional[DateRange]
    updated_date: Optional[DateRange]
    tracked_date: Optional[DateRange]
    me: Optional[StrictBool]
    descendants: Optional[StrictBool]
    sub_tasks: Optional[StrictBool]
    plain_text: Optional[StrictBool]
    timelog_categories: Optional[Sequence[TimelogCategoryId]]
    billing_types: Optional[Sequence[BillingType]]
    fields_: Optional[Sequence[Literal[TimelogOptionalFields.BILLING_TYPE]]] = Field(None, alias="fields")

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

        if self.created_date:
            params["createdDate"] = self._convert_input(self.created_date)

        if self.updated_date:
            params["updatedDate"] = self._convert_input(self.updated_date)

        if self.tracked_date:
            params[" trackedDate"] = self._convert_input(self.tracked_date)

        if self.me is not None:
            params["me"] = self._convert_bool(self.me)

        if self.descendants is not None:
            params["descendants"] = self._convert_bool(self.descendants)

        if self.sub_tasks is not None:
            params["subTasks"] = self._convert_bool(self.sub_tasks)

        if self.plain_text is not None:
            params["plainText"] = self._convert_bool(self.plain_text)

        if self.timelog_categories is not None:
            params["timelogCategories"] = self._convert_seq(self.timelog_categories)

        if self.billing_types is not None:
            params["billingTypes"] = self._convert_seq(self.billing_types)

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class Timelogs(_BaseTimelogs):
    @property
    def _url(self) -> str:
        return "/timelogs"


class ContactTimelogs(_BaseTimelogs):
    contact_id: ContactId

    @property
    def _url(self) -> str:
        return f"/contacts/{self.contact_id}/timelogs"


class FolderTimelogs(_BaseTimelogs):
    folder_id: FolderId

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/timelogs"


class TaskTimelogs(_BaseTimelogs):
    task_id: TaskId

    @property
    def _url(self) -> str:
        return f"/tasks/{self.task_id}/timelogs"


class TimelogCategoryTimelogs(_BaseTimelogs):
    timelog_category_id: TimelogCategoryId

    @property
    def _url(self) -> str:
        return f"/timelog_categories/{self.timelog_category_id}/timelogs"


class TimelogsById(BaseEndpoint):
    timelog_ids: Sequence[TimelogId] = Field(..., max_length=100)
    plain_text: Optional[StrictBool]
    fields_: Optional[Sequence[Literal[TimelogOptionalFields.BILLING_TYPE]]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/timelogs/{','.join(self.timelog_ids)}",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.plain_text is not None:
            params["plainText"] = self._convert_bool(self.plain_text)

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class _CreateOrModifyTimelog(BaseEndpoint):
    plain_text: Optional[StrictBool]
    category_id: Optional[TimelogCategoryId]
    fields_: Optional[Sequence[Literal[TimelogOptionalFields.BILLING_TYPE]]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method=self._method,
            url=self._url,
            body_params=self._body_params,
        )

    @property
    def _url(self) -> str:
        raise NotImplementedError()

    @property
    def _method(self) -> Methods:
        raise NotImplementedError()

    @property
    def _body_params(self) -> BodyParams:
        params = {}

        if self.plain_text is not None:
            params["plainText"] = self._convert_bool(self.plain_text)

        if self.category_id is not None:
            params["categoryId"] = self.category_id

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class CreateTimelog(_CreateOrModifyTimelog):
    task_id: TaskId
    comment: str
    hours: int
    tracked_date: date

    @property
    def _url(self) -> str:
        return f"/tasks/{self.task_id}/timelogs"

    @property
    def _method(self) -> Methods:
        return "POST"

    @property
    def _body_params(self) -> BodyParams:
        params = super()._body_params
        return {
            **params,
            **{"comment": self.comment, "hours": str(self.hours), "trackedDate": self.tracked_date.isoformat()},
        }


class ModifyTimelog(_CreateOrModifyTimelog):
    timelog_id: TimelogId
    comment: Optional[str]
    hours: Optional[int]
    tracked_date: Optional[date]

    @property
    def _url(self) -> str:
        return f"/timelogs/{self.timelog_id}"

    @property
    def _method(self) -> Methods:
        return "PUT"

    @property
    def _body_params(self) -> BodyParams:
        params = super()._body_params

        if self.comment is not None:
            params["comment"] = self.comment

        if self.hours is not None:
            params["hours"] = str(self.hours)

        if self.tracked_date:
            params["trackedDate"] = self.tracked_date.isoformat()

        return params


class DeleteTimelog(BaseEndpoint):
    timelog_id: TimelogId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/timelogs/{self.timelog_id}",
        )
