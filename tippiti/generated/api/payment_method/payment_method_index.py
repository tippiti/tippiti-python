from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.payment_method_index_response_200 import PaymentMethodIndexResponse200
from ...models.payment_method_index_response_401 import PaymentMethodIndexResponse401
from ...models.payment_method_index_response_403 import PaymentMethodIndexResponse403
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/billing/payment-methods",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403 | None:
    if response.status_code == 200:
        response_200 = PaymentMethodIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PaymentMethodIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PaymentMethodIndexResponse403.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403]:
    """ List stored payment methods

     Returns the billing account's saved payment methods, with the default
    method first, followed by the remainder in reverse chronological order.
    Each entry includes the gateway, a display label, the optional
    description and whether it is the default. Available to main users and
    to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403]
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

) -> PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403 | None:
    """ List stored payment methods

     Returns the billing account's saved payment methods, with the default
    method first, followed by the remainder in reverse chronological order.
    Each entry includes the gateway, a display label, the optional
    description and whether it is the default. Available to main users and
    to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403]:
    """ List stored payment methods

     Returns the billing account's saved payment methods, with the default
    method first, followed by the remainder in reverse chronological order.
    Each entry includes the gateway, a display label, the optional
    description and whether it is the default. Available to main users and
    to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403]
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

) -> PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403 | None:
    """ List stored payment methods

     Returns the billing account's saved payment methods, with the default
    method first, followed by the remainder in reverse chronological order.
    Each entry includes the gateway, a display label, the optional
    description and whether it is the default. Available to main users and
    to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodIndexResponse200 | PaymentMethodIndexResponse401 | PaymentMethodIndexResponse403
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
