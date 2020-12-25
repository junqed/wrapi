from __future__ import annotations

from datetime import date
from typing import Optional

from ..api import (
    BodyParams,
    EndpointData,
    WrApiQueryParams,
)
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import ExclusionType
from ..types_.inputs import WorkScheduleDateRangeEqual
from ..types_.scalar import WorkScheduleExclusionId, WorkScheduleId


class WorkScheduleExclusionById(BaseEndpoint):
    work_schedule_exclusion_id: WorkScheduleExclusionId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/workschedule_exclusions/{self.work_schedule_exclusion_id}",
        )


class WorkScheduleExclusionForWorkSchedule(BaseEndpoint):
    work_schedule_id: WorkScheduleId
    date_range: Optional[WorkScheduleDateRangeEqual]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/workschedules/{self.work_schedule_id}/workschedule_exclusions",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.date_range:
            params["dateRange"] = self._convert_input(self.date_range)

        return params


class CreateWorkScheduleExclusion(BaseEndpoint):
    work_schedule_id: WorkScheduleId
    from_date: date
    to_date: date
    exclusion_type: ExclusionType

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url=f"/workschedules/{self.work_schedule_id}/workschedule_exclusions",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        return {
            "fromDate": self.from_date.isoformat(),
            "toDate": self.to_date.isoformat(),
            "exclusionType": self.exclusion_type.value,
        }


class ModifyWorkScheduleExclusion(BaseEndpoint):
    work_schedule_exclusion_id: WorkScheduleExclusionId

    from_date: Optional[date]
    to_date: Optional[date]
    exclusion_type: Optional[ExclusionType]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url=f"/workschedule_exclusions/{self.work_schedule_exclusion_id}",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        body = {}

        if self.from_date:
            body["fromDate"] = self.from_date.isoformat()

        if self.to_date:
            body["toDate"] = self.to_date.isoformat()

        if self.exclusion_type:
            body["exclusionType"] = self.exclusion_type.value

        return body


class DeleteWorkScheduleExclusion(BaseEndpoint):
    work_schedule_exclusion_id: WorkScheduleExclusionId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/workschedule_exclusions/{self.work_schedule_exclusion_id}",
        )
