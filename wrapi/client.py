from __future__ import annotations

import typing as t
from contextlib import asynccontextmanager, contextmanager

from httpx import AsyncClient, Client

from . import __version__
from .auth import WrikePermanentTokenAuth


DEFAULT_BASE_URL = "https://www.wrike.com/api/v4"
DEFAULT_USER_AGENT = f"Wrike Api Client v{__version__}"


@contextmanager
def client(
    auth: t.Union[WrikePermanentTokenAuth],
    url: str = DEFAULT_BASE_URL,
) -> t.Generator[Client, None, None]:
    with Client(base_url=url, auth=auth, headers={"User-Agent": DEFAULT_USER_AGENT}) as c:
        yield c


@asynccontextmanager
async def async_client(
    auth: t.Union[WrikePermanentTokenAuth],
    url: str = DEFAULT_BASE_URL,
) -> t.AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(base_url=url, auth=auth, headers={"User-Agent": DEFAULT_USER_AGENT}) as c:
        yield c
