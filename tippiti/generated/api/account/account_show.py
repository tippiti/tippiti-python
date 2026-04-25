from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_show_response_200 import AccountShowResponse200
from ...models.account_show_response_401 import AccountShowResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountShowResponse200 | AccountShowResponse401 | None:
    if response.status_code == 200:
        response_200 = AccountShowResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountShowResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccountShowResponse200 | AccountShowResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountShowResponse200 | AccountShowResponse401]:
    """ Get account profile

     Returns the authenticated account's profile, billing details, verification
    status and resolved permissions. Sub-users receive a reduced view –
    billing and balance fields are only present when the sub-user has the
    corresponding capabilities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountShowResponse200 | AccountShowResponse401]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> AccountShowResponse200 | AccountShowResponse401 | None:
    """ Get account profile

     Returns the authenticated account's profile, billing details, verification
    status and resolved permissions. Sub-users receive a reduced view –
    billing and balance fields are only present when the sub-user has the
    corresponding capabilities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountShowResponse200 | AccountShowResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountShowResponse200 | AccountShowResponse401]:
    """ Get account profile

     Returns the authenticated account's profile, billing details, verification
    status and resolved permissions. Sub-users receive a reduced view –
    billing and balance fields are only present when the sub-user has the
    corresponding capabilities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountShowResponse200 | AccountShowResponse401]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> AccountShowResponse200 | AccountShowResponse401 | None:
    """ Get account profile

     Returns the authenticated account's profile, billing details, verification
    status and resolved permissions. Sub-users receive a reduced view –
    billing and balance fields are only present when the sub-user has the
    corresponding capabilities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountShowResponse200 | AccountShowResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
