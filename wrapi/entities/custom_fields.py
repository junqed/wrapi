from __future__ import annotations

from typing import Sequence

from ..types_.entity import BaseEntity
from ..types_.enums import CustomFieldType
from ..types_.outputs import CustomFieldSettings
from ..types_.scalar import (
    AccountId,
    ContactId,
    CustomFieldId,
)


class CustomField(BaseEntity):
    id: CustomFieldId
    account_id: AccountId
    title: str
    type: CustomFieldType
    shared_ids: Sequence[ContactId]
    settings: CustomFieldSettings
