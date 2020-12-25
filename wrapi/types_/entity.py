from __future__ import annotations

from pydantic import BaseModel as PydanticBaseModel


class BaseEntity(PydanticBaseModel):
    class Config:
        allow_mutation = False

        @classmethod
        def alias_generator(cls, s: str) -> str:
            # this is the same as `alias_generator = to_camel` above
            return "".join(word.capitalize() if i != 0 else word for i, word in enumerate(s.split("_")))
