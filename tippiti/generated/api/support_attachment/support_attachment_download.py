from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.support_attachment_download_response_200 import SupportAttachmentDownloadResponse200
from ...models.support_attachment_download_response_401 import SupportAttachmentDownloadResponse401
from ...models.support_attachment_download_response_403 import SupportAttachmentDownloadResponse403
from ...models.support_attachment_download_response_404 import SupportAttachmentDownloadResponse404
from typing import cast



def _get_kwargs(
    attachment: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/support/attachments/{attachment}/download".format(attachment=quote(str(attachment), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404 | None:
    if response.status_code == 200:
        response_200 = SupportAttachmentDownloadResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = SupportAttachmentDownloadResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SupportAttachmentDownloadResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SupportAttachmentDownloadResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attachment: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404]:
    """ Download a support ticket attachment

     Streams the binary content of a file attached to a support ticket that
    the authenticated account is allowed to view. Available to main users
    and to sub-users with the support-access capability.

    Args:
        attachment (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404]
     """


    kwargs = _get_kwargs(
        attachment=attachment,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    attachment: str,
    *,
    client: AuthenticatedClient | Client,

) -> SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404 | None:
    """ Download a support ticket attachment

     Streams the binary content of a file attached to a support ticket that
    the authenticated account is allowed to view. Available to main users
    and to sub-users with the support-access capability.

    Args:
        attachment (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404
     """


    return sync_detailed(
        attachment=attachment,
client=client,

    ).parsed

async def asyncio_detailed(
    attachment: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404]:
    """ Download a support ticket attachment

     Streams the binary content of a file attached to a support ticket that
    the authenticated account is allowed to view. Available to main users
    and to sub-users with the support-access capability.

    Args:
        attachment (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404]
     """


    kwargs = _get_kwargs(
        attachment=attachment,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    attachment: str,
    *,
    client: AuthenticatedClient | Client,

) -> SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404 | None:
    """ Download a support ticket attachment

     Streams the binary content of a file attached to a support ticket that
    the authenticated account is allowed to view. Available to main users
    and to sub-users with the support-access capability.

    Args:
        attachment (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportAttachmentDownloadResponse200 | SupportAttachmentDownloadResponse401 | SupportAttachmentDownloadResponse403 | SupportAttachmentDownloadResponse404
     """


    return (await asyncio_detailed(
        attachment=attachment,
client=client,

    )).parsed
