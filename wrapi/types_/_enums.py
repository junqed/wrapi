from __future__ import annotations

from enum import Enum
from typing import Any


class NameEnum(Enum):
    """
    FOLDER_BLUEPRINT_LAUNCH -> FOLDER_BLUEPRINT_LAUNCH
    """

    @staticmethod
    def _generate_next_value_(name: str, start: Any, count: Any, last_values: Any) -> str:
        return name


class CapitalizedNameEnum(Enum):
    """
    FOLDER_BLUEPRINT_LAUNCH -> FolderBlueprintLaunch
    """

    @staticmethod
    def _generate_next_value_(name: str, start: Any, count: Any, last_values: Any) -> str:
        return "".join(map(lambda x: x.capitalize(), name.split("_")))


class CapitalizedExceptFirstNameEnum(Enum):
    """
    SUPER_PARENT_IDS -> superParentIds
    """

    @staticmethod
    def _generate_next_value_(name: str, start: Any, count: Any, last_values: Any) -> str:
        return "".join(map(lambda x: x[1].capitalize() if x[0] != 0 else x[1].lower(), enumerate(name.split("_"))))
