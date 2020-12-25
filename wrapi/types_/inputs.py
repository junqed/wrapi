from __future__ import annotations

from datetime import date, datetime
from enum import auto
from typing import (
    Optional,
    Sequence,
    Union,
)

from pydantic.fields import Field

from ._enums import CapitalizedExceptFirstNameEnum, CapitalizedNameEnum
from .endpoint import BaseEndpoint
from .enums import (
    Aggregation,
    BillingType,
    Currency,
    CustomFieldComparator,
    CustomStatusColor,
    InheritanceType,
    ProjectStatus,
    TaskEffortMode,
    TaskStatus,
    TaskType,
    UserRole,
    WeekDay,
)
from .scalar import (
    AccessRoleId,
    AccountId,
    ContactId,
    CustomFieldId,
    CustomStatusId,
    HEXColor,
)


class ContactsOptionalFields(str, CapitalizedExceptFirstNameEnum):
    METADATA = auto()
    WORK_SCHEDULE_ID = auto()


class TimelogOptionalFields(str, CapitalizedExceptFirstNameEnum):
    BILLING_TYPE = auto()


class ShortTaskOptionalFields(str, CapitalizedExceptFirstNameEnum):
    EFFORT_ALLOCATION = auto()
    BILLING_TYPE = auto()


class WorkScheduleFields(str, CapitalizedExceptFirstNameEnum):
    user_ids = auto()


class TaskOptionalFields(ShortTaskOptionalFields):
    AUTHOR_IDS = auto()
    HAS_ATTACHMENTS = auto()
    ATTACHMENT_COUNT = auto()
    PARENT_IDS = auto()
    SUPER_PARENT_IDS = auto()
    SHARED_IDS = auto()
    RESPONSIBLE_IDS = auto()
    DESCRIPTION = auto()
    BRIEF_DESCRIPTION = auto()
    RECURRENT = auto()
    SUPER_TASK_IDS = auto()
    SUB_TASK_IDS = auto()
    DEPENDENCY_IDS = auto()
    METADATA = auto()
    CUSTOM_FIELDS = auto()


class TaskReschedulingMode(str, CapitalizedNameEnum):
    START = auto()
    END = auto()


class TaskDates(BaseEndpoint):
    type: TaskType
    duration: int
    start: datetime
    due: datetime
    work_on_weekends: Optional[bool]


class TaskEffort(BaseEndpoint):
    mode: TaskEffortMode
    total_effort: Optional[int]
    allocated_effort: Optional[int]


class FolderOptionalFields(str, CapitalizedExceptFirstNameEnum):
    METADATA = auto()
    HAS_ATTACHMENTS = auto()
    ATTACHMENT_COUNT = auto()
    DESCRIPTION = auto()
    BRIEF_DESCRIPTION = auto()
    CUSTOM_FIELDS = auto()
    CUSTOM_COLUMN_IDS = auto()
    SUPER_PARENT_IDS = auto()
    SPACE = auto()
    CONTRACT_TYPE = auto()


class AccountOptionalFields(str, CapitalizedExceptFirstNameEnum):
    SUBSCRIPTION = auto()
    METADATA = auto()
    CUSTOM_FIELDS = auto()


class SpaceOptionalFields(str, CapitalizedExceptFirstNameEnum):
    MEMBERS = auto()


class SpaceAccessType(str, CapitalizedNameEnum):
    PRIVATE = auto()
    PUBLIC = auto()


class ApprovalFinalStatus(str, CapitalizedNameEnum):
    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()
    CANCELLED = auto()
    DRAFT = auto()


class EDiscoverySearchScope(str, CapitalizedExceptFirstNameEnum):
    TASK = auto()
    FOLDER = auto()
    PROJECT = auto()
    SPACE = auto()
    ATTACHMENT = auto()


class CustomField(BaseEndpoint):
    id: CustomFieldId
    value: str


class CustomFieldFilter(BaseEndpoint):
    id: str
    comparator: Optional[CustomFieldComparator]
    value: Optional[str]
    min_value: Optional[str]
    max_value: Optional[str]
    values: Optional[Sequence[str]]


class TaskDatetimeRangeEqualFilter(BaseEndpoint):
    start: Optional[Union[date, datetime]]
    end: Optional[Union[date, datetime]]
    equal: Optional[bool]


class TaskDatetimeRangeFilter(BaseEndpoint):
    start: Optional[datetime]
    end: Optional[datetime]


class TaskDateRangeEqualFilter(BaseEndpoint):
    start: Optional[date]
    end: Optional[date]
    equal: Optional[bool]


class WorkScheduleDateRangeEqual(BaseEndpoint):
    start: Optional[date]
    end: Optional[date]
    equal: Optional[date]


class Metadata(BaseEndpoint):
    key: str = Field(..., max_length=50, regex=r"([A-Za-z0-9_-]+)")
    value: str = Field(..., max_length=1000)


class Profile(BaseEndpoint):
    account_id: AccountId
    role: UserRole
    external: Optional[bool]


class Avatar(BaseEndpoint):
    letters: str = Field(..., max_length=2)
    color: HEXColor


class GroupUpdate(BaseEndpoint):
    id: ContactId
    add_members: Optional[Sequence[ContactId]]
    remove_members: Optional[Sequence[ContactId]]


class WorkflowCustomField(BaseEndpoint):
    name: str
    standard_name: bool
    color: CustomStatusColor
    standard: bool
    group: TaskStatus
    hidden: bool


class CustomFieldSettings(BaseEndpoint):
    inheritance_type: Optional[InheritanceType]
    decimal_places: Optional[int]
    use_thousands_separator: Optional[bool]
    currency: Optional[Currency]
    aggregation: Optional[Aggregation]
    values: Optional[Sequence[str]]
    allow_other_values: Optional[bool]
    contacts: Optional[Sequence[ContactId]]


class DateRange(BaseEndpoint):
    start: Optional[datetime]
    end: Optional[datetime]


class Project(BaseEndpoint):
    owner_ids: Optional[Sequence[ContactId]]
    status: Optional[ProjectStatus]
    custom_status_id: Optional[CustomStatusId]
    start_date: Optional[date]
    end_date: Optional[date]
    contract_type: Optional[BillingType]


class SpaceMember(BaseEndpoint):
    id: ContactId
    access_role_id: AccessRoleId
    is_manager: bool


class WorkWeek(BaseEndpoint):
    day_of_week: WeekDay
    is_work_day: bool
