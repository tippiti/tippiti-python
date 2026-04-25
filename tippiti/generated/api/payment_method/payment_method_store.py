from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.payment_method_store_body import PaymentMethodStoreBody
from ...models.payment_method_store_response_201 import PaymentMethodStoreResponse201
from ...models.payment_method_store_response_401 import PaymentMethodStoreResponse401
from ...models.payment_method_store_response_403 import PaymentMethodStoreResponse403
from ...models.payment_method_store_response_422 import PaymentMethodStoreResponse422
from typing import cast



def _get_kwargs(
    *,
    body: PaymentMethodStoreBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing/payment-methods",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422 | None:
    if response.status_code == 201:
        response_201 = PaymentMethodStoreResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = PaymentMethodStoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PaymentMethodStoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PaymentMethodStoreResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PaymentMethodStoreBody,

) -> Response[PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422]:
    """ Store a new payment method

     Confirms a payment method previously collected via a setup intent and
    attaches it to the authenticated main user's billing account. Requires
    the gateway's `payment_method_id`; the optional `gateway` parameter
    currently accepts `stripe`. Returns the stored payment method. Main
    users only.

    Args:
        body (PaymentMethodStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422]
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
    body: PaymentMethodStoreBody,

) -> PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422 | None:
    """ Store a new payment method

     Confirms a payment method previously collected via a setup intent and
    attaches it to the authenticated main user's billing account. Requires
    the gateway's `payment_method_id`; the optional `gateway` parameter
    currently accepts `stripe`. Returns the stored payment method. Main
    users only.

    Args:
        body (PaymentMethodStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PaymentMethodStoreBody,

) -> Response[PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422]:
    """ Store a new payment method

     Confirms a payment method previously collected via a setup intent and
    attaches it to the authenticated main user's billing account. Requires
    the gateway's `payment_method_id`; the optional `gateway` parameter
    currently accepts `stripe`. Returns the stored payment method. Main
    users only.

    Args:
        body (PaymentMethodStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422]
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
    body: PaymentMethodStoreBody,

) -> PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422 | None:
    """ Store a new payment method

     Confirms a payment method previously collected via a setup intent and
    attaches it to the authenticated main user's billing account. Requires
    the gateway's `payment_method_id`; the optional `gateway` parameter
    currently accepts `stripe`. Returns the stored payment method. Main
    users only.

    Args:
        body (PaymentMethodStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodStoreResponse201 | PaymentMethodStoreResponse401 | PaymentMethodStoreResponse403 | PaymentMethodStoreResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
