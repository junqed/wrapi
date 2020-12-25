from __future__ import annotations

from typing import Any, Iterable

from pydantic import BaseModel


class BaseEndpoint(BaseModel):
    class Config:
        allow_mutation = False
        allow_population_by_field_name = True

        @classmethod
        def alias_generator(cls, s: str) -> str:
            # this is the same as `alias_generator = to_camel` above
            return "".join(word.capitalize() if i != 0 else word for i, word in enumerate(s.split("_")))

    @staticmethod
    def _convert_seq(seq: Iterable[Any]) -> str:
        return "".join(("[", ",".join(f'"{field}"' for field in seq), "]"))

    @staticmethod
    def _convert_input_seq(seq: Iterable[BaseModel]) -> str:
        return "".join(("[", ",".join(f"{BaseEndpoint._convert_input(field)}" for field in seq), "]"))

    @staticmethod
    def _convert_input(model: BaseModel) -> str:
        return model.json(exclude_none=True, by_alias=True, separators=(",", ":"))

    @staticmethod
    def _convert_bool(value: bool) -> str:
        if value:
            return "true"
        else:
            return "false"
