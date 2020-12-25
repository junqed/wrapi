from __future__ import annotations

from datetime import date, datetime
from enum import auto
from typing import Optional, Sequence

from ._enums import CapitalizedNameEnum
from .entity import BaseEntity
from .enums import (
    Aggregation,
    BillingType,
    Currency,
    CustomStatusColor,
    InheritanceType,
    ProjectStatus,
    SubscriptionType,
    TaskEffortMode,
    TaskStatus,
    TaskType,
)
from .scalar import (
    AccessRoleId,
    ContactId,
    CustomFieldId,
    CustomStatusId,
)


class AsyncJobStatus(str, CapitalizedNameEnum):
    IN_QUEUE = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    FAILED = auto()


class AsyncJobType(str, CapitalizedNameEnum):
    COPY_FOLDER = auto()
    FOLDER_BLUEPRINT_LAUNCH = auto()


class UserType(str, CapitalizedNameEnum):
    PERSON = auto()
    GROUP = auto()


class UserRole(str, CapitalizedNameEnum):
    USER = auto()
    COLLABORATOR = auto()


class SpaceAccessType(str, CapitalizedNameEnum):
    PRIVATE = auto()
    PUBLIC = auto()
    PERSONAL = auto()


class WorkScheduleType(str, CapitalizedNameEnum):
    DEFAULT = auto()
    CUSTOM = auto()


class AuditObjectType(str, CapitalizedNameEnum):
    USER = auto()
    ACCOUNT = auto()
    TASK = auto()
    FOLDER = auto()
    PROJECT = auto()
    COMMENT = auto()
    ATTACHMENT = auto()
    INVITATION = auto()
    GROUP = auto()
    CUSTOM_FIELD = auto()
    OAUTH2_CLIENT = auto()
    REQUEST_FORM = auto()
    WORKFLOW = auto()
    CALENDAR_EXTERNAL_LINK = auto()
    WORKSPACE_SNAPSHOT = auto()
    DATA_EXPORT = auto()
    ACCESS_ROLE = auto()
    SPACE = auto()
    ANALYZE_REPORT = auto()
    ANALYZE_REPORT_WIDGET = auto()
    POWER_BI_ENTITY = "PowerBIEntity"


class ApprovalStatus(str, CapitalizedNameEnum):
    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()


class ApprovalType(str, CapitalizedNameEnum):
    REGULAR = auto()
    FILES_ONLY = auto()


class TaskDates(BaseEntity):
    type: TaskType
    duration: Optional[int]
    start: Optional[datetime]
    due: Optional[datetime]
    work_on_weekends: Optional[bool]


class Metadata(BaseEntity):
    key: str
    value: str


class CustomField(BaseEntity):
    id: CustomFieldId
    value: str


class WorkflowCustomField(BaseEntity):
    id: CustomFieldId
    name: str
    standard_name: bool
    color: CustomStatusColor
    standard: bool
    group: TaskStatus
    hidden: bool


class TaskEffort(BaseEntity):
    mode: TaskEffortMode
    total_effort: Optional[int]
    allocated_effort: Optional[int]


class Subscription(BaseEntity):
    type: SubscriptionType
    suspended: bool
    paid: bool
    user_limit: int


class CustomFieldSettings(BaseEntity):
    inheritance_type: InheritanceType
    decimal_places: Optional[int]
    use_thousands_separator: Optional[bool]
    currency: Optional[Currency]
    aggregation: Optional[Aggregation]
    values: Optional[Sequence[str]]
    allow_other_values: Optional[bool]
    contacts: Optional[Sequence[ContactId]]
    read_only: bool


class Project(BaseEntity):
    author_id: Optional[ContactId]
    owner_ids: Sequence[ContactId]
    status: ProjectStatus
    custom_status_id: Optional[CustomStatusId]
    start_date: Optional[date]
    end_date: Optional[date]
    created_date: Optional[datetime]
    completed_date: Optional[datetime]
    contract_type: Optional[BillingType]


class SpaceMember(BaseEntity):
    id: ContactId
    access_role_id: AccessRoleId
    is_manager: bool


class DataExportResource(BaseEntity):
    name: str
    url: str


class ApprovalDecision(BaseEntity):
    approver_id: ContactId
    comment: str
    status: ApprovalStatus
    updated_date: datetime
