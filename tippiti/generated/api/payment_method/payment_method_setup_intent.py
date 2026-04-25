from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.payment_method_setup_intent_body import PaymentMethodSetupIntentBody
from ...models.payment_method_setup_intent_response_200 import PaymentMethodSetupIntentResponse200
from ...models.payment_method_setup_intent_response_401 import PaymentMethodSetupIntentResponse401
from ...models.payment_method_setup_intent_response_403 import PaymentMethodSetupIntentResponse403
from ...models.payment_method_setup_intent_response_422 import PaymentMethodSetupIntentResponse422
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: PaymentMethodSetupIntentBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing/payment-methods/setup-intent",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422 | None:
    if response.status_code == 200:
        response_200 = PaymentMethodSetupIntentResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PaymentMethodSetupIntentResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PaymentMethodSetupIntentResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PaymentMethodSetupIntentResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PaymentMethodSetupIntentBody | Unset = UNSET,

) -> Response[PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422]:
    """ Create a setup intent for adding a payment method

     Returns a gateway client secret that the caller uses to collect new
    payment-method details on the client side before confirming them via
    the store endpoint. The optional `gateway` parameter currently accepts
    `stripe`. Main users only.

    Args:
        body (PaymentMethodSetupIntentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422]
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
    body: PaymentMethodSetupIntentBody | Unset = UNSET,

) -> PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422 | None:
    """ Create a setup intent for adding a payment method

     Returns a gateway client secret that the caller uses to collect new
    payment-method details on the client side before confirming them via
    the store endpoint. The optional `gateway` parameter currently accepts
    `stripe`. Main users only.

    Args:
        body (PaymentMethodSetupIntentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PaymentMethodSetupIntentBody | Unset = UNSET,

) -> Response[PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422]:
    """ Create a setup intent for adding a payment method

     Returns a gateway client secret that the caller uses to collect new
    payment-method details on the client side before confirming them via
    the store endpoint. The optional `gateway` parameter currently accepts
    `stripe`. Main users only.

    Args:
        body (PaymentMethodSetupIntentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422]
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
    body: PaymentMethodSetupIntentBody | Unset = UNSET,

) -> PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422 | None:
    """ Create a setup intent for adding a payment method

     Returns a gateway client secret that the caller uses to collect new
    payment-method details on the client side before confirming them via
    the store endpoint. The optional `gateway` parameter currently accepts
    `stripe`. Main users only.

    Args:
        body (PaymentMethodSetupIntentBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodSetupIntentResponse200 | PaymentMethodSetupIntentResponse401 | PaymentMethodSetupIntentResponse403 | PaymentMethodSetupIntentResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
