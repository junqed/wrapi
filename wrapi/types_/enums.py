from __future__ import annotations

from enum import Enum, auto

from ._enums import (
    CapitalizedExceptFirstNameEnum,
    CapitalizedNameEnum,
    NameEnum,
)


class TaskStatus(str, CapitalizedNameEnum):
    ACTIVE = auto()
    COMPLETED = auto()
    DEFERRED = auto()
    CANCELLED = auto()


class TaskImportance(str, CapitalizedNameEnum):
    HIGH = auto()
    NORMAL = auto()
    LOW = auto()


class TaskType(str, CapitalizedNameEnum):
    BACKLOG = auto()
    MILESTONE = auto()
    PLANNED = auto()


class TaskSortFilter(str, CapitalizedNameEnum):
    CREATED_DATE = auto()
    UPDATED_DATE = auto()
    COMPLETED_DATE = auto()
    DUE_DATE = auto()
    START_FINISH_INTERVAL = auto()
    STATUS = auto()
    IMPORTANCE = auto()
    TITLE = auto()
    LAST_ACCESS_DATE = auto()


class TaskSortOrder(str, CapitalizedNameEnum):
    ASC = auto()
    DESC = auto()


class CustomFieldComparator(str, CapitalizedNameEnum):
    EQUAL_TO = auto()
    IS_EMPTY = auto()
    IS_NOT_EMPTY = auto()
    LESS_THAN = auto()
    LESS_OR_EQUAL_TO = auto()
    GREATER_THAN = auto()
    GREATER_OR_EQUAL_TO = auto()
    IN_RANGE = auto()
    NOT_IN_RANGE = auto()
    CONTAINS = auto()
    STARTS_WITH = auto()
    ENDS_WITH = auto()
    CONTAINS_ALL = auto()
    CONTAINS_ANY = auto()


class TreeScope(str, CapitalizedNameEnum):
    WS_ROOT = auto()
    RB_ROOT = auto()
    WS_FOLDER = auto()
    RB_FOLDER = auto()
    WS_TASK = auto()
    RB_TASK = auto()


class BillingType(str, CapitalizedNameEnum):
    BILLABLE = auto()
    NON_BILLABLE = auto()


class TaskEffortMode(str, CapitalizedNameEnum):
    NONE = auto()
    FULL_TIME = auto()
    BASIC = auto()
    FLEXIBLE = auto()


class UserRole(str, CapitalizedNameEnum):
    USER = auto()
    COLLABORATOR = auto()


class V2EntityType(str, CapitalizedNameEnum):
    API_V2_ACCOUNT = auto()
    API_V2_USER = auto()
    API_V2_FOLDER = auto()
    API_V2_TASK = auto()
    API_V2_COMMENT = auto()
    API_V2_ATTACHMENT = auto()
    API_V2_TIMELOG = auto()


class InvitationStatus(str, CapitalizedNameEnum):
    PENDING = auto()
    ACCEPTED = auto()
    DECLINED = auto()
    CANCELLED = auto()


class WeekDay(str, CapitalizedNameEnum):
    SAT = auto()
    SUN = auto()
    MON = auto()
    TUE = auto()
    WED = auto()
    THU = auto()
    FRI = auto()


class SubscriptionType(str, CapitalizedNameEnum):
    FREE = auto()
    PREMIUM = auto()
    BUSINESS = auto()
    CREATIVE_BUSINESS = auto()
    ENTERPRISE = auto()
    CREATIVE_ENTERPRISE = auto()


class CustomFieldType(str, CapitalizedNameEnum):
    TEXT = auto()
    DROP_DOWN = auto()
    NUMERIC = auto()
    CURRENCY = auto()
    PERCENTAGE = auto()
    DATE = auto()
    DURATION = auto()
    CHECKBOX = auto()
    CONTACTS = auto()
    MULTIPLE = auto()


class CustomStatusColor(str, CapitalizedNameEnum):
    BROWN = auto()
    RED = auto()
    PURPLE = auto()
    INDIGO = auto()
    DARK_BLUE = auto()
    BLUE = auto()
    TURQUOISE = auto()
    DARK_CYAN = auto()
    GREEN = auto()
    YELLOW_GREEN = auto()
    YELLOW = auto()
    ORANGE = auto()
    GRAY = auto()


class InheritanceType(str, CapitalizedNameEnum):
    ALL = auto()
    FOLDERS = auto()
    PROJECTS = auto()
    TASKS = auto()


class Currency(str, NameEnum):
    USD = auto()
    EUR = auto()
    GBP = auto()
    RUB = auto()
    BRL = auto()
    AED = auto()
    ARS = auto()
    BYR = auto()
    CAD = auto()
    CLP = auto()
    COP = auto()
    CZK = auto()
    DKK = auto()
    HKD = auto()
    HUF = auto()
    INR = auto()
    IDR = auto()
    ILS = auto()
    JPY = auto()
    KRW = auto()
    MYR = auto()
    MXN = auto()
    NZD = auto()
    NOK = auto()
    PEN = auto()
    PHP = auto()
    PLN = auto()
    QAR = auto()
    RON = auto()
    SAR = auto()
    SGD = auto()
    ZAR = auto()
    SEK = auto()
    CHF = auto()
    TWD = auto()
    THB = auto()
    TRY = auto()
    UAH = auto()
    VND = auto()
    CNY = auto()
    AUD = auto()
    AMD = auto()
    BWP = auto()


class Aggregation(str, CapitalizedNameEnum):
    NONE = auto()
    SUM = auto()
    AVERAGE = auto()


class Color(str, CapitalizedNameEnum):
    NONE = auto()
    PERSON = auto()
    PURPLE1 = auto()
    PURPLE2 = auto()
    PURPLE3 = auto()
    PURPLE4 = auto()
    INDIGO1 = auto()
    INDIGO2 = auto()
    INDIGO3 = auto()
    INDIGO4 = auto()
    DARK_BLUE1 = auto()
    DARK_BLUE2 = auto()
    DARK_BLUE3 = auto()
    DARK_BLUE4 = auto()
    BLUE1 = auto()
    BLUE2 = auto()
    BLUE3 = auto()
    BLUE4 = auto()
    TURQUOISE1 = auto()
    TURQUOISE2 = auto()
    TURQUOISE3 = auto()
    TURQUOISE4 = auto()
    DARK_CYAN1 = auto()
    DARK_CYAN2 = auto()
    DARK_CYAN3 = auto()
    DARK_CYAN4 = auto()
    GREEN1 = auto()
    GREEN2 = auto()
    GREEN3 = auto()
    GREEN4 = auto()
    YELLOW_GREEN1 = auto()
    YELLOW_GREEN2 = auto()
    YELLOW_GREEN3 = auto()
    YELLOW_GREEN4 = auto()
    YELLOW1 = auto()
    YELLOW2 = auto()
    YELLOW3 = auto()
    YELLOW4 = auto()
    ORANGE1 = auto()
    ORANGE2 = auto()
    ORANGE3 = auto()
    ORANGE4 = auto()
    RED1 = auto()
    RED2 = auto()
    RED3 = auto()
    RED4 = auto()
    PINK1 = auto()
    PINK2 = auto()
    PINK3 = auto()
    PINK4 = auto()
    GRAY1 = auto()
    GRAY2 = auto()
    GRAY3 = auto()


class ProjectStatus(str, CapitalizedNameEnum):
    GREEN = auto()
    YELLOW = auto()
    RED = auto()
    COMPLETED = auto()
    ON_HOLD = auto()
    CANCELLED = auto()
    CUSTOM = auto()


class DependencyRelationType(str, CapitalizedNameEnum):
    START_TO_START = auto()
    START_TO_FINISH = auto()
    FINISH_TO_START = auto()
    FINISH_TO_FINISH = auto()


class Size(str, CapitalizedExceptFirstNameEnum):
    W44 = auto()
    W100 = auto()
    W200 = auto()
    W300 = auto()
    W400 = auto()
    H400 = auto()


class AttachmentType(str, Enum):
    WRIKE = "Wrike"
    GOOGLE = "Google"
    DROPBOX = "DropBox"
    BOX = "Box"
    ONEDRIVE = "OneDrive"
    SHAREPOINT = "SharePoint"
    EXTERNAL = "External"
    DAM = "DAM"


class DataExportVersion(str, CapitalizedNameEnum):
    V0 = auto()
    V1 = auto()


class DataExportStatus(str, CapitalizedNameEnum):
    SCHEDULED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELLED = auto()
    FAILED = auto()


class ColumnDataType(str, CapitalizedNameEnum):
    NUMBER = auto()
    STRING = auto()
    DATE = auto()
    BOOLEAN = auto()


class AuditLogOperation(str, CapitalizedNameEnum):
    USER_LOGGED_IN = auto()
    USER_FAIL_LOGIN = auto()
    USER_LOGOUT = auto()
    ADMIN_LOGGED_IN_AS_USER = auto()
    ONE_TIME_PASSWORD_CREATED = auto()
    ONE_TIME_PASSWORD_USED = auto()
    ONE_TIME_PASSWORD_REVOKED = auto()
    USER_ROLE_CHANGED = auto()
    USER_ADMIN_PERMISSIONS_CHANGED = auto()
    USER_GRANT_ADMIN = auto()
    USER_REVOKE_ADMIN = auto()
    USER_DEACTIVATED = auto()
    USER_ACTIVATED = auto()
    USERS_AND_GROUPS_EXPORTED = auto()
    INVITATION_SEND = auto()
    INVITATION_ACCEPTED = auto()
    ATTACH_UPLOADED = auto()
    ATTACH_DELETED = auto()
    ATTACH_MOVED = auto()
    ATTACH_COPIED = auto()
    GROUP_CREATED = auto()
    GROUP_MEMBER_ADDED = auto()
    GROUP_MEMBER_REMOVED = auto()
    GROUP_RENAMED = auto()
    GROUP_DELETED = auto()
    GROUP_PARENT_ADDED = auto()
    GROUP_PARENT_REMOVED = auto()
    TASK_CREATED = auto()
    TASK_PARENT_ADDED = auto()
    TASK_PARENT_REMOVED = auto()
    TASK_SHARED = auto()
    TASK_UNSHARED = auto()
    TASK_ASSIGNED = auto()
    TASK_UNASSIGNED = auto()
    TASK_DELETED = auto()
    TASK_ERASED = auto()
    TIMELOG_LOCKED = auto()
    TIMELOG_UNLOCKED = auto()
    TASK_COMMENT_CHANGED = auto()
    TASK_COMMENT_DELETED = auto()
    RECYCLE_BIN_ERASED = auto()
    TASK_STATUS_CHANGED = auto()
    TASK_DUPLICATION = auto()
    USER_DELETED = auto()
    USER_RESTORED = auto()
    APPROVER_ADDED = auto()
    APPROVER_REMOVED = auto()
    APPROVAL_DESCRIPTION_CHANGED = auto()
    APPROVAL_DUE_DATE_CHANGED = auto()
    APPROVAL_CREATED = auto()
    APPROVAL_FINISHED = auto()
    APPROVAL_CANCELED = auto()
    APPROVAL_DECISION_MADE = auto()
    CUSTOM_FIELD_CREATED = auto()
    CUSTOM_FIELD_MODIFIED = auto()
    CUSTOM_FIELD_REMOVED = auto()
    CUSTOM_FIELD_RESTORED = auto()
    CUSTOM_FIELD_ADDED_TO_FOLDER = auto()
    CUSTOM_FIELD_REMOVED_FROM_FOLDER = auto()
    SECOND_FACTOR_ENABLED = auto()
    SECOND_FACTOR_DISABLED = auto()
    SECOND_FACTOR_USAGE_REPORT_CREATED = auto()
    AUDIT_REPORT_CREATED = auto()
    ACCOUNT_BACKUP_CREATED = auto()
    ACCOUNT_MODIFIED = auto()
    ACCOUNT_DELETED = auto()
    OAUTH2_ACCESS_GRANTED = auto()
    OAUTH2_ACCESS_REVOKED = auto()
    FEED_CREATED = auto()
    EXCEL_EXPORT_CREATED = auto()
    ACCESS_AUDIT_REPORT_CSV_EXPORT = auto()
    USER_PROFILE_UPDATED = auto()
    PASSWORD_CHANGED = auto()
    PASSWORD_POLICY_MODIFIED = auto()
    APPROVED_IP_RANGES_OR_SUBNETS_CHANGED = auto()
    INVITATION_POLICY_CHANGED = auto()
    REQUEST_FORM_CREATED = auto()
    REQUEST_FORM_MODIFIED = auto()
    REQUEST_FORM_DELETED = auto()
    ACCESS_ROLE_CREATED = auto()
    ACCESS_ROLE_MODIFIED = auto()
    ACCESS_ROLE_DELETED = auto()
    WORKFLOW_CREATED = auto()
    WORKFLOW_DELETED = auto()
    WORKFLOW_MODIFIED = auto()
    CALENDAR_EXTERNAL_LINKS_DEACTIVATED = auto()
    CALENDAR_EXTERNAL_LINKS_ACTIVATED = auto()
    CALENDAR_EXTERNAL_LINK_CREATED = auto()
    CALENDAR_EXTERNAL_LINK_DELETED = auto()
    ANALYZE_PUBLIC_LINK_CREATED = auto()
    ANALYZE_PUBLIC_LINK_DELETED = auto()
    ANALYZE_PUBLIC_LINK_ACCESSED = auto()
    ANALYZE_WIDGET_PUBLIC_LINK_CREATED = auto()
    ANALYZE_WIDGET_PUBLIC_LINK_DELETED = auto()
    ANALYZE_WIDGET_PUBLIC_LINK_ACCESSED = auto()
    POWER_BI_PUBLIC_LINK_CREATED = "PowerBIPublicLinkCreated"
    POWER_BI_PUBLIC_LINK_DELETED = "PowerBIPublicLinkDeleted"
    POWER_BI_PUBLIC_LINK_ACCESSED = "PowerBIPublicLinkAccessed"
    GUEST_REVIEWER_INVITED = auto()
    GUEST_REVIEWER_CHANGED = auto()
    GUEST_REVIEWER_REVOKED = auto()
    GUEST_REVIEW_ACCEPTED = auto()
    GUEST_REVIEW_REJECTED = auto()
    GUEST_REVIEW_ACCOUNT_SETTINGS_CHANGED = auto()
    GANTT_SNAPSHOT_CREATED = auto()
    GANTT_SNAPSHOT_DELETED = auto()
    USER_TASK_GROUP_ROLES_CHANGED = auto()
    ACCOUNT_DATA_EXPORT_REQUESTED = auto()
    ACCOUNT_DATA_EXPORT_GENERATED = auto()
    SAML_SSO_ENABLED = "SamlSSOEnabled"
    SAML_SSO_DISABLED = "SamlSSODisabled"
    SAML_SSO_SETTINGS_CHANGED = "SamlSSOSettingsChanged"
    SAML_SSO_METADATA_CHANGED = "SamlSSOMetadataChanged"
    SAML_CLEAR_PASSWORD_FOR_SAML_USERS = auto()
    ONE_TIME_PASSWORD_STATUS_SWITCHED = auto()
    ACCESS_CODE_GENERATED = auto()
    ACCESS_CODE_ACCEPTED = auto()
    ACCESS_CODE_DECLINED = auto()
    APPROVED_DOMAINS_CHANGED = auto()
    ADMIN_MAIL_SETTINGS_CHANGED = auto()
    SPACE_CREATED = auto()
    SPACE_DELETED = auto()
    SPACE_ARCHIVED_UNARCHIVED = auto()
    USER_JOINED_SPACE = auto()
    USER_LEFT_SPACE = auto()


class ExclusionType(str, CapitalizedNameEnum):
    ADDITIONAL_WORK_DAYS = auto()
    PUBLIC_HOLIDAYS = auto()
    OTHER_EVENT = auto()


class UserExclusionType(str, CapitalizedNameEnum):
    OVERTIME = auto()
    VACATION_PTO = "VacationPTO"
    OTHER_NON_WORKING = auto()
