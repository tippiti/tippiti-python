from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.payment_method_destroy_response_200 import PaymentMethodDestroyResponse200
from ...models.payment_method_destroy_response_401 import PaymentMethodDestroyResponse401
from ...models.payment_method_destroy_response_403 import PaymentMethodDestroyResponse403
from ...models.payment_method_destroy_response_404 import PaymentMethodDestroyResponse404
from typing import cast



def _get_kwargs(
    payment_method: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/billing/payment-methods/{payment_method}".format(payment_method=quote(str(payment_method), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404 | None:
    if response.status_code == 200:
        response_200 = PaymentMethodDestroyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PaymentMethodDestroyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PaymentMethodDestroyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PaymentMethodDestroyResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    payment_method: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404]:
    """ Delete a payment method

     Removes the specified payment method from the authenticated main
    user's billing account and detaches it from the gateway. Only payment
    methods belonging to the account may be deleted. Main users only.

    Args:
        payment_method (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404]
     """


    kwargs = _get_kwargs(
        payment_method=payment_method,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    payment_method: str,
    *,
    client: AuthenticatedClient | Client,

) -> PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404 | None:
    """ Delete a payment method

     Removes the specified payment method from the authenticated main
    user's billing account and detaches it from the gateway. Only payment
    methods belonging to the account may be deleted. Main users only.

    Args:
        payment_method (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404
     """


    return sync_detailed(
        payment_method=payment_method,
client=client,

    ).parsed

async def asyncio_detailed(
    payment_method: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404]:
    """ Delete a payment method

     Removes the specified payment method from the authenticated main
    user's billing account and detaches it from the gateway. Only payment
    methods belonging to the account may be deleted. Main users only.

    Args:
        payment_method (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404]
     """


    kwargs = _get_kwargs(
        payment_method=payment_method,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    payment_method: str,
    *,
    client: AuthenticatedClient | Client,

) -> PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404 | None:
    """ Delete a payment method

     Removes the specified payment method from the authenticated main
    user's billing account and detaches it from the gateway. Only payment
    methods belonging to the account may be deleted. Main users only.

    Args:
        payment_method (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodDestroyResponse200 | PaymentMethodDestroyResponse401 | PaymentMethodDestroyResponse403 | PaymentMethodDestroyResponse404
     """


    return (await asyncio_detailed(
        payment_method=payment_method,
client=client,

    )).parsed
