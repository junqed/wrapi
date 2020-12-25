from __future__ import annotations

import typing as t
from abc import abstractmethod
from dataclasses import dataclass
from urllib.parse import quote, urlencode

from httpx import (
    AsyncClient,
    Client,
    QueryParams,
    Request,
)
from pydantic.generics import GenericModel


T = t.TypeVar("T")

Methods = t.Literal["POST", "GET", "PUT", "DELETE"]
BodyParams = t.Dict[str, str]


class WrikeResponse(GenericModel, t.Generic[T]):
    kind: str
    data: T


@dataclass(frozen=True)
class EndpointData:
    method: Methods
    url: str
    query_params: t.Optional[WrApiQueryParams] = None
    body_params: t.Optional[BodyParams] = None


class EndpointProto(t.Protocol):  # pragma: no cover
    @property
    @abstractmethod
    def endpoint_data(self) -> EndpointData:
        ...


class Query:
    def __init__(self, req: Request, client: Client):
        self.req = req
        self.client = client

    def as_model(self, return_type: t.Type[T]) -> T:
        resp = self.client.send(self.req)
        resp.raise_for_status()
        typed_resp_model = WrikeResponse[return_type]  # type: ignore

        return typed_resp_model.parse_raw(resp.read()).data

    def as_raw(self) -> bytes:
        resp = self.client.send(self.req)
        resp.raise_for_status()
        return resp.read()

    def as_json(self) -> t.Any:
        resp = self.client.send(self.req)
        resp.raise_for_status()
        return resp.json()

    def ignored(self) -> None:
        resp = self.client.send(self.req)
        resp.raise_for_status()


class AsyncQuery:
    def __init__(self, req: Request, client: AsyncClient):
        self.req = req
        self.client = client

    async def as_model(self, return_type: t.Type[T]) -> T:
        resp = await self.client.send(self.req)
        resp.raise_for_status()

        typed_resp_model = WrikeResponse[return_type]  # type: ignore
        return typed_resp_model.parse_raw(await resp.aread()).data

    async def as_raw(self) -> bytes:
        resp = await self.client.send(self.req)
        resp.raise_for_status()

        return await resp.aread()

    async def as_json(self) -> t.Any:
        resp = await self.client.send(self.req)
        resp.raise_for_status()

        return resp.json()

    async def ignored(self) -> None:
        resp = await self.client.send(self.req)
        resp.raise_for_status()


@t.overload
def query(client: Client, endpoint: EndpointProto) -> Query:
    ...


@t.overload
def query(client: AsyncClient, endpoint: EndpointProto) -> AsyncQuery:  # noqa: F811
    ...


def query(client: t.Union[Client, AsyncClient], endpoint: EndpointProto) -> t.Union[Query, AsyncQuery]:  # noqa: F811
    endpoint_data = endpoint.endpoint_data
    headers = {}
    body = ""

    if endpoint_data.body_params:
        # Wrike uses it's own method of working with urls
        # so it's needed to be encode the other way :(
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = str(WrApiQueryParams(endpoint_data.body_params))

    req = client.build_request(
        method=endpoint_data.method,
        # small hack to workaround buggy wrike api because it doesn't take quoted parameters
        # but the default implementation in httpx tries to encode relatives paths
        url=client.base_url.join(endpoint_data.url.lstrip("/")),
        headers=headers,
        params=WrApiQueryParams(endpoint_data.query_params),
        content=body,
    )

    if isinstance(client, Client):
        return Query(req=req, client=client)
    else:
        return AsyncQuery(req=req, client=client)


# def paged(endpoint: EndpointProto) -> t.NoReturn:
#     raise NotImplementedError()


class WrApiQueryParams(QueryParams):
    def __str__(self) -> str:
        # Wrike uses it's own method of working with urls
        # so it's needed to be encode the other way :(
        return urlencode(self._list, safe='[]:{}", ', quote_via=quote)
