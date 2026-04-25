from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_share_store_body import DictationShareStoreBody
from ...models.dictation_share_store_response_201 import DictationShareStoreResponse201
from ...models.dictation_share_store_response_401 import DictationShareStoreResponse401
from ...models.dictation_share_store_response_403 import DictationShareStoreResponse403
from ...models.dictation_share_store_response_404 import DictationShareStoreResponse404
from ...models.dictation_share_store_response_422 import DictationShareStoreResponse422
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    dictation: str,
    *,
    body: DictationShareStoreBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/{dictation}/shares".format(dictation=quote(str(dictation), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422 | None:
    if response.status_code == 201:
        response_201 = DictationShareStoreResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = DictationShareStoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationShareStoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationShareStoreResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationShareStoreResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareStoreBody | Unset = UNSET,

) -> Response[DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422]:
    """ Create a share for a dictation

     Creates a share record that lets recipients view the dictation via
    the public `/shared/{token}` flow. Optional fields include a
    `password`, an `expires_at` timestamp and the recipient permissions
    `allow_delete`, `allow_archive` and `show_notes`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareStoreBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareStoreBody | Unset = UNSET,

) -> DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422 | None:
    """ Create a share for a dictation

     Creates a share record that lets recipients view the dictation via
    the public `/shared/{token}` flow. Optional fields include a
    `password`, an `expires_at` timestamp and the recipient permissions
    `allow_delete`, `allow_archive` and `show_notes`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareStoreBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422
     """


    return sync_detailed(
        dictation=dictation,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareStoreBody | Unset = UNSET,

) -> Response[DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422]:
    """ Create a share for a dictation

     Creates a share record that lets recipients view the dictation via
    the public `/shared/{token}` flow. Optional fields include a
    `password`, an `expires_at` timestamp and the recipient permissions
    `allow_delete`, `allow_archive` and `show_notes`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareStoreBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareStoreBody | Unset = UNSET,

) -> DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422 | None:
    """ Create a share for a dictation

     Creates a share record that lets recipients view the dictation via
    the public `/shared/{token}` flow. Optional fields include a
    `password`, an `expires_at` timestamp and the recipient permissions
    `allow_delete`, `allow_archive` and `show_notes`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareStoreBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareStoreResponse201 | DictationShareStoreResponse401 | DictationShareStoreResponse403 | DictationShareStoreResponse404 | DictationShareStoreResponse422
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,
body=body,

    )).parsed
