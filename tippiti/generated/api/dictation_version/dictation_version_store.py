from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_version_store_response_201 import DictationVersionStoreResponse201
from ...models.dictation_version_store_response_401 import DictationVersionStoreResponse401
from ...models.dictation_version_store_response_403 import DictationVersionStoreResponse403
from ...models.dictation_version_store_response_404 import DictationVersionStoreResponse404
from ...models.dictation_version_store_response_422 import DictationVersionStoreResponse422
from ...models.save_version_request import SaveVersionRequest
from typing import cast



def _get_kwargs(
    dictation: str,
    *,
    body: SaveVersionRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/{dictation}/versions".format(dictation=quote(str(dictation), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422 | None:
    if response.status_code == 201:
        response_201 = DictationVersionStoreResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = DictationVersionStoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationVersionStoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationVersionStoreResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationVersionStoreResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422]:
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
    body: SaveVersionRequest,

) -> Response[DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422]:
    """ Create a new version of a dictation

     Creates a new active version with the supplied text and an optional
    change summary. The new version receives the next sequential version
    number. Requires the parent dictation to be completed and the caller
    to have edit rights on the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (SaveVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422]
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
    body: SaveVersionRequest,

) -> DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422 | None:
    """ Create a new version of a dictation

     Creates a new active version with the supplied text and an optional
    change summary. The new version receives the next sequential version
    number. Requires the parent dictation to be completed and the caller
    to have edit rights on the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (SaveVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422
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
    body: SaveVersionRequest,

) -> Response[DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422]:
    """ Create a new version of a dictation

     Creates a new active version with the supplied text and an optional
    change summary. The new version receives the next sequential version
    number. Requires the parent dictation to be completed and the caller
    to have edit rights on the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (SaveVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422]
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
    body: SaveVersionRequest,

) -> DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422 | None:
    """ Create a new version of a dictation

     Creates a new active version with the supplied text and an optional
    change summary. The new version receives the next sequential version
    number. Requires the parent dictation to be completed and the caller
    to have edit rights on the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (SaveVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationVersionStoreResponse201 | DictationVersionStoreResponse401 | DictationVersionStoreResponse403 | DictationVersionStoreResponse404 | DictationVersionStoreResponse422
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,
body=body,

    )).parsed
