from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.folder_update_body import FolderUpdateBody
from ...models.folder_update_response_200 import FolderUpdateResponse200
from ...models.folder_update_response_401 import FolderUpdateResponse401
from ...models.folder_update_response_403 import FolderUpdateResponse403
from ...models.folder_update_response_404 import FolderUpdateResponse404
from ...models.folder_update_response_422 import FolderUpdateResponse422
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    folder: str,
    *,
    body: FolderUpdateBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/folders/{folder}".format(folder=quote(str(folder), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = FolderUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = FolderUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = FolderUpdateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = FolderUpdateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = FolderUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422]:
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
    body: FolderUpdateBody | Unset = UNSET,

) -> Response[FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422]:
    """ Update a folder

     Renames a folder or moves it to a new parent. Main users only.
    Moving a folder beneath one of its own descendants is rejected. Names
    must be unique within the target parent.

    Args:
        folder (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (FolderUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422]
     """


    kwargs = _get_kwargs(
        folder=folder,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    body: FolderUpdateBody | Unset = UNSET,

) -> FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422 | None:
    """ Update a folder

     Renames a folder or moves it to a new parent. Main users only.
    Moving a folder beneath one of its own descendants is rejected. Names
    must be unique within the target parent.

    Args:
        folder (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (FolderUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422
     """


    return sync_detailed(
        folder=folder,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    body: FolderUpdateBody | Unset = UNSET,

) -> Response[FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422]:
    """ Update a folder

     Renames a folder or moves it to a new parent. Main users only.
    Moving a folder beneath one of its own descendants is rejected. Names
    must be unique within the target parent.

    Args:
        folder (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (FolderUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422]
     """


    kwargs = _get_kwargs(
        folder=folder,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    folder: str,
    *,
    client: AuthenticatedClient | Client,
    body: FolderUpdateBody | Unset = UNSET,

) -> FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422 | None:
    """ Update a folder

     Renames a folder or moves it to a new parent. Main users only.
    Moving a folder beneath one of its own descendants is rejected. Names
    must be unique within the target parent.

    Args:
        folder (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (FolderUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderUpdateResponse200 | FolderUpdateResponse401 | FolderUpdateResponse403 | FolderUpdateResponse404 | FolderUpdateResponse422
     """


    return (await asyncio_detailed(
        folder=folder,
client=client,
body=body,

    )).parsed
