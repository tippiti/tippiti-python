from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.folder_store_body import FolderStoreBody
from ...models.folder_store_response_201 import FolderStoreResponse201
from ...models.folder_store_response_401 import FolderStoreResponse401
from ...models.folder_store_response_403 import FolderStoreResponse403
from ...models.folder_store_response_422 import FolderStoreResponse422
from typing import cast



def _get_kwargs(
    *,
    body: FolderStoreBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/folders",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422 | None:
    if response.status_code == 201:
        response_201 = FolderStoreResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = FolderStoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = FolderStoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = FolderStoreResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FolderStoreBody,

) -> Response[FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422]:
    """ Create a folder

     Creates a new folder in the authenticated account's folder tree.
    Main users only; sub-users cannot create folders. An optional
    `parent_id` nests the folder beneath an existing one; the parent must
    belong to the same account. Folder names must be unique within the same
    parent.

    Args:
        body (FolderStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: FolderStoreBody,

) -> FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422 | None:
    """ Create a folder

     Creates a new folder in the authenticated account's folder tree.
    Main users only; sub-users cannot create folders. An optional
    `parent_id` nests the folder beneath an existing one; the parent must
    belong to the same account. Folder names must be unique within the same
    parent.

    Args:
        body (FolderStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: FolderStoreBody,

) -> Response[FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422]:
    """ Create a folder

     Creates a new folder in the authenticated account's folder tree.
    Main users only; sub-users cannot create folders. An optional
    `parent_id` nests the folder beneath an existing one; the parent must
    belong to the same account. Folder names must be unique within the same
    parent.

    Args:
        body (FolderStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: FolderStoreBody,

) -> FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422 | None:
    """ Create a folder

     Creates a new folder in the authenticated account's folder tree.
    Main users only; sub-users cannot create folders. An optional
    `parent_id` nests the folder beneath an existing one; the parent must
    belong to the same account. Folder names must be unique within the same
    parent.

    Args:
        body (FolderStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderStoreResponse201 | FolderStoreResponse401 | FolderStoreResponse403 | FolderStoreResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
