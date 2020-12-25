from __future__ import annotations

from typing import Optional, Sequence

from pydantic.fields import Field

from ..api import (
    BodyParams,
    EndpointData,
    Methods,
    WrApiQueryParams,
)
from ..types_.endpoint import BaseEndpoint
from ..types_.inputs import WorkScheduleFields, WorkWeek
from ..types_.scalar import ContactId, WorkScheduleId


class _WorkSchedulesBaseEndpoint(BaseEndpoint):
    fields_: Optional[Sequence[WorkScheduleFields]] = Field(None, alias="fields")

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

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params

    @property
    def _url(self) -> str:
        raise NotImplementedError()


class WorkSchedules(_WorkSchedulesBaseEndpoint):
    @property
    def _url(self) -> str:
        return "/workschedules"


class WorkScheduleById(_WorkSchedulesBaseEndpoint):
    work_schedule_id: WorkScheduleId

    @property
    def _url(self) -> str:
        return f"/workschedules/{self.work_schedule_id}"


class _CreateOrModifyWorkSchedule(BaseEndpoint):
    add_users: Optional[Sequence[ContactId]]
    fields_: Optional[Sequence[WorkScheduleFields]] = Field(None, alias="fields")

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

        if self.add_users:
            body["addUsers"] = self._convert_seq(self.add_users)

        if self.fields_:
            body["fields"] = self._convert_seq(self.fields_)

        return body

    @property
    def _url(self) -> str:
        raise NotImplementedError()

    @property
    def _method(self) -> Methods:
        raise NotImplementedError()


class CreateWorkSchedule(_CreateOrModifyWorkSchedule):
    title: str
    workweek: Sequence[WorkWeek]

    @property
    def _url(self) -> str:
        return "/workschedules"

    @property
    def _method(self) -> Methods:
        return "POST"

    @property
    def _body_params(self) -> BodyParams:
        body = {"title": self.title, "workweek": self._convert_input_seq(self.workweek)}
        return {**super()._body_params, **body}


class ModifyWorkSchedule(_CreateOrModifyWorkSchedule):
    work_schedule_id: WorkScheduleId

    title: Optional[str]
    workweek: Optional[Sequence[WorkWeek]]
    remove_users: Optional[Sequence[ContactId]]

    @property
    def _url(self) -> str:
        return f"/workschedules/{self.work_schedule_id}"

    @property
    def _method(self) -> Methods:
        return "PUT"

    @property
    def _body_params(self) -> BodyParams:
        body = super()._body_params

        if self.title is not None:
            body["title"] = self.title

        if self.workweek:
            body["workweek"] = self._convert_input_seq(self.workweek)

        if self.remove_users:
            body["removeUsers"] = self._convert_seq(self.remove_users)

        return body


class DeleteWorkSchedule(BaseEndpoint):
    work_schedule_id: WorkScheduleId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/workschedules/{self.work_schedule_id}",
        )
