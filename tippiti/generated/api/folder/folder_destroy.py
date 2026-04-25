from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.folder_destroy_response_200 import FolderDestroyResponse200
from ...models.folder_destroy_response_401 import FolderDestroyResponse401
from ...models.folder_destroy_response_403 import FolderDestroyResponse403
from ...models.folder_destroy_response_404 import FolderDestroyResponse404
from typing import cast



def _get_kwargs(
    folder: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/folders/{folder}".format(folder=quote(str(folder), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404 | None:
    if response.status_code == 200:
        response_200 = FolderDestroyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = FolderDestroyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = FolderDestroyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = FolderDestroyResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    folder: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404]:
    """ Delete a folder

     Deletes a folder belonging to the authenticated account. Main users
    only. Any references to the folder in sub-user access grants are
    cleaned up automatically.

    Args:
        folder (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404]
     """


    kwargs = _get_kwargs(
        folder=folder,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    folder: str,
    *,
    client: AuthenticatedClient | Client,

) -> FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404 | None:
    """ Delete a folder

     Deletes a folder belonging to the authenticated account. Main users
    only. Any references to the folder in sub-user access grants are
    cleaned up automatically.

    Args:
        folder (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404
     """


    return sync_detailed(
        folder=folder,
client=client,

    ).parsed

async def asyncio_detailed(
    folder: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404]:
    """ Delete a folder

     Deletes a folder belonging to the authenticated account. Main users
    only. Any references to the folder in sub-user access grants are
    cleaned up automatically.

    Args:
        folder (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404]
     """


    kwargs = _get_kwargs(
        folder=folder,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    folder: str,
    *,
    client: AuthenticatedClient | Client,

) -> FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404 | None:
    """ Delete a folder

     Deletes a folder belonging to the authenticated account. Main users
    only. Any references to the folder in sub-user access grants are
    cleaned up automatically.

    Args:
        folder (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderDestroyResponse200 | FolderDestroyResponse401 | FolderDestroyResponse403 | FolderDestroyResponse404
     """


    return (await asyncio_detailed(
        folder=folder,
client=client,

    )).parsed
