from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_pricing_response_200 import AccountPricingResponse200
from ...models.account_pricing_response_401 import AccountPricingResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/account/pricing",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountPricingResponse200 | AccountPricingResponse401 | None:
    if response.status_code == 200:
        response_200 = AccountPricingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountPricingResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccountPricingResponse200 | AccountPricingResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountPricingResponse200 | AccountPricingResponse401]:
    """ Get current pricing

     Returns pricing applicable to the authenticated account: price per 1,000
    characters (may be account-specific), minimum top-up amount, applicable
    VAT rate and tax status (derived from the account's country and tax ID).
    All amounts are in EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountPricingResponse200 | AccountPricingResponse401]
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

) -> AccountPricingResponse200 | AccountPricingResponse401 | None:
    """ Get current pricing

     Returns pricing applicable to the authenticated account: price per 1,000
    characters (may be account-specific), minimum top-up amount, applicable
    VAT rate and tax status (derived from the account's country and tax ID).
    All amounts are in EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountPricingResponse200 | AccountPricingResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AccountPricingResponse200 | AccountPricingResponse401]:
    """ Get current pricing

     Returns pricing applicable to the authenticated account: price per 1,000
    characters (may be account-specific), minimum top-up amount, applicable
    VAT rate and tax status (derived from the account's country and tax ID).
    All amounts are in EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountPricingResponse200 | AccountPricingResponse401]
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

) -> AccountPricingResponse200 | AccountPricingResponse401 | None:
    """ Get current pricing

     Returns pricing applicable to the authenticated account: price per 1,000
    characters (may be account-specific), minimum top-up amount, applicable
    VAT rate and tax status (derived from the account's country and tax ID).
    All amounts are in EUR.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountPricingResponse200 | AccountPricingResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
