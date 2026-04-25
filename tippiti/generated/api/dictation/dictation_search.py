from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_search_response_200 import DictationSearchResponse200
from ...models.dictation_search_response_401 import DictationSearchResponse401
from ...models.dictation_search_response_403 import DictationSearchResponse403
from ...models.dictation_search_response_422 import DictationSearchResponse422
from typing import cast



def _get_kwargs(
    *,
    q: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dictations/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationSearchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationSearchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationSearchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = DictationSearchResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,

) -> Response[DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422]:
    """ Search dictations by title, metadata and transcript content

     Accepts a `q` query string of 2 to 255 characters and returns matching
    dictations the caller has access to. Main users search across their
    own dictations; sub-users search only within the dictations their
    permissions expose.

    Args:
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422]
     """


    kwargs = _get_kwargs(
        q=q,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str,

) -> DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422 | None:
    """ Search dictations by title, metadata and transcript content

     Accepts a `q` query string of 2 to 255 characters and returns matching
    dictations the caller has access to. Main users search across their
    own dictations; sub-users search only within the dictations their
    permissions expose.

    Args:
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422
     """


    return sync_detailed(
        client=client,
q=q,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,

) -> Response[DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422]:
    """ Search dictations by title, metadata and transcript content

     Accepts a `q` query string of 2 to 255 characters and returns matching
    dictations the caller has access to. Main users search across their
    own dictations; sub-users search only within the dictations their
    permissions expose.

    Args:
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422]
     """


    kwargs = _get_kwargs(
        q=q,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str,

) -> DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422 | None:
    """ Search dictations by title, metadata and transcript content

     Accepts a `q` query string of 2 to 255 characters and returns matching
    dictations the caller has access to. Main users search across their
    own dictations; sub-users search only within the dictations their
    permissions expose.

    Args:
        q (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationSearchResponse200 | DictationSearchResponse401 | DictationSearchResponse403 | DictationSearchResponse422
     """


    return (await asyncio_detailed(
        client=client,
q=q,

    )).parsed
