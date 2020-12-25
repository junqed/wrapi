from __future__ import annotations

import typing as t

from httpx import (
    Auth,
    Request,
    Response,
)


WRIKE_AUTH_HEADER_NAME = "Authorization"


class WrikePermanentTokenAuth(Auth):
    def __init__(self, permanent_token: str):
        self.permanent_token = permanent_token

    def auth_flow(self, request: Request) -> t.Generator[Request, Response, None]:
        request.headers[WRIKE_AUTH_HEADER_NAME] = f"bearer {self.permanent_token}"
        yield request


class WrikeRefreshTokenAuth(Auth):
    def __init__(self, access_token: t.Optional[str], refresh_token: str, client_id: str, client_secret: str):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret

    def auth_flow(self, request: Request) -> t.Generator[Request, Response, None]:
        raise NotImplementedError()
