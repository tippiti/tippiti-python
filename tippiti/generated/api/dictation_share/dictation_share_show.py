from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_share_show_response_200 import DictationShareShowResponse200
from ...models.dictation_share_show_response_401 import DictationShareShowResponse401
from ...models.dictation_share_show_response_403 import DictationShareShowResponse403
from ...models.dictation_share_show_response_404 import DictationShareShowResponse404
from typing import cast



def _get_kwargs(
    share: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/shares/{share}".format(share=quote(str(share), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationShareShowResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationShareShowResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationShareShowResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationShareShowResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404]:
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

) -> Response[DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404]:
    """ Get a share

     Returns a single share belonging to the authenticated account with
    its recipient emails, view records, dictation reference and owner.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404]
     """


    kwargs = _get_kwargs(
        share=share,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    share: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404 | None:
    """ Get a share

     Returns a single share belonging to the authenticated account with
    its recipient emails, view records, dictation reference and owner.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404
     """


    return sync_detailed(
        share=share,
client=client,

    ).parsed

async def asyncio_detailed(
    share: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404]:
    """ Get a share

     Returns a single share belonging to the authenticated account with
    its recipient emails, view records, dictation reference and owner.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404]
     """


    kwargs = _get_kwargs(
        share=share,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    share: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404 | None:
    """ Get a share

     Returns a single share belonging to the authenticated account with
    its recipient emails, view records, dictation reference and owner.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareShowResponse200 | DictationShareShowResponse401 | DictationShareShowResponse403 | DictationShareShowResponse404
     """


    return (await asyncio_detailed(
        share=share,
client=client,

    )).parsed
