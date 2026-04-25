from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_share_update_body import DictationShareUpdateBody
from ...models.dictation_share_update_response_200 import DictationShareUpdateResponse200
from ...models.dictation_share_update_response_401 import DictationShareUpdateResponse401
from ...models.dictation_share_update_response_403 import DictationShareUpdateResponse403
from ...models.dictation_share_update_response_404 import DictationShareUpdateResponse404
from ...models.dictation_share_update_response_422 import DictationShareUpdateResponse422
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    share: str,
    *,
    body: DictationShareUpdateBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/shares/{share}".format(share=quote(str(share), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationShareUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationShareUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationShareUpdateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationShareUpdateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationShareUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareUpdateBody | Unset = UNSET,

) -> Response[DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422]:
    """ Update a share's settings

     Updates access controls on an existing share – password (set a new
    one via `password` or clear it with `remove_password`), expiry (set
    `expires_at` or clear with `remove_expiry`) and the flags
    `allow_delete`, `allow_archive` and `show_notes`. Only supplied
    fields are changed.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422]
     """


    kwargs = _get_kwargs(
        share=share,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareUpdateBody | Unset = UNSET,

) -> DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422 | None:
    """ Update a share's settings

     Updates access controls on an existing share – password (set a new
    one via `password` or clear it with `remove_password`), expiry (set
    `expires_at` or clear with `remove_expiry`) and the flags
    `allow_delete`, `allow_archive` and `show_notes`. Only supplied
    fields are changed.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422
     """


    return sync_detailed(
        share=share,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareUpdateBody | Unset = UNSET,

) -> Response[DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422]:
    """ Update a share's settings

     Updates access controls on an existing share – password (set a new
    one via `password` or clear it with `remove_password`), expiry (set
    `expires_at` or clear with `remove_expiry`) and the flags
    `allow_delete`, `allow_archive` and `show_notes`. Only supplied
    fields are changed.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422]
     """


    kwargs = _get_kwargs(
        share=share,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareUpdateBody | Unset = UNSET,

) -> DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422 | None:
    """ Update a share's settings

     Updates access controls on an existing share – password (set a new
    one via `password` or clear it with `remove_password`), expiry (set
    `expires_at` or clear with `remove_expiry`) and the flags
    `allow_delete`, `allow_archive` and `show_notes`. Only supplied
    fields are changed.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareUpdateResponse200 | DictationShareUpdateResponse401 | DictationShareUpdateResponse403 | DictationShareUpdateResponse404 | DictationShareUpdateResponse422
     """


    return (await asyncio_detailed(
        share=share,
client=client,
body=body,

    )).parsed
