from __future__ import annotations

from datetime import date
from typing import Optional, Sequence

from ..api import (
    BodyParams,
    EndpointData,
    WrApiQueryParams,
)
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import UserExclusionType
from ..types_.inputs import WorkScheduleDateRangeEqual
from ..types_.scalar import ContactId, WorkScheduleExclusionId


class UserScheduleExclusions(BaseEndpoint):
    date_range: Optional[WorkScheduleDateRangeEqual]
    user_ids: Optional[Sequence[ContactId]]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url="/user_schedule_exclusions",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.date_range:
            params["dateRange"] = self._convert_input(self.date_range)

        if self.user_ids:
            params["userIds"] = self._convert_seq(self.user_ids)

        return params


class UserScheduleExclusionById(BaseEndpoint):
    user_schedule_exclusion_id: WorkScheduleExclusionId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/user_schedule_exclusions/{self.user_schedule_exclusion_id}",
        )


class CreateUserScheduleExclusion(BaseEndpoint):
    user_id: ContactId
    from_date: date
    to_date: date
    exclusion_type: UserExclusionType

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url="/user_schedule_exclusions",
            body_params=self._body_params,
        )

    @property
    def _body_params(self) -> BodyParams:
        return {
            "fromDate": self.from_date.isoformat(),
            "toDate": self.to_date.isoformat(),
            "exclusionType": self.exclusion_type.value,
            "user_id": self.user_id,
        }


class ModifyUserScheduleExclusion(BaseEndpoint):
    user_schedule_exclusion_id: WorkScheduleExclusionId

    from_date: Optional[date]
    to_date: Optional[date]
    exclusion_type: Optional[UserExclusionType]

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="PUT",
            url=f"/user_schedule_exclusions/{self.user_schedule_exclusion_id}",
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


class DeleteUserScheduleExclusion(BaseEndpoint):
    user_schedule_exclusion_id: WorkScheduleExclusionId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/user_schedule_exclusions/{self.user_schedule_exclusion_id}",
        )
