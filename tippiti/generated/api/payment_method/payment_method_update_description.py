from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.payment_method_update_description_body import PaymentMethodUpdateDescriptionBody
from ...models.payment_method_update_description_response_200 import PaymentMethodUpdateDescriptionResponse200
from ...models.payment_method_update_description_response_401 import PaymentMethodUpdateDescriptionResponse401
from ...models.payment_method_update_description_response_403 import PaymentMethodUpdateDescriptionResponse403
from ...models.payment_method_update_description_response_404 import PaymentMethodUpdateDescriptionResponse404
from ...models.payment_method_update_description_response_422 import PaymentMethodUpdateDescriptionResponse422
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    payment_method: str,
    *,
    body: PaymentMethodUpdateDescriptionBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/billing/payment-methods/{payment_method}".format(payment_method=quote(str(payment_method), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422 | None:
    if response.status_code == 200:
        response_200 = PaymentMethodUpdateDescriptionResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PaymentMethodUpdateDescriptionResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PaymentMethodUpdateDescriptionResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PaymentMethodUpdateDescriptionResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PaymentMethodUpdateDescriptionResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422]:
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
    body: PaymentMethodUpdateDescriptionBody | Unset = UNSET,

) -> Response[PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422]:
    """ Update a payment method's description

     Sets a free-text description (max 100 characters, nullable) on the
    specified payment method. Only payment methods belonging to the
    authenticated main user may be updated. Returns the updated payment
    method. Main users only.

    Args:
        payment_method (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (PaymentMethodUpdateDescriptionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422]
     """


    kwargs = _get_kwargs(
        payment_method=payment_method,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    payment_method: str,
    *,
    client: AuthenticatedClient | Client,
    body: PaymentMethodUpdateDescriptionBody | Unset = UNSET,

) -> PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422 | None:
    """ Update a payment method's description

     Sets a free-text description (max 100 characters, nullable) on the
    specified payment method. Only payment methods belonging to the
    authenticated main user may be updated. Returns the updated payment
    method. Main users only.

    Args:
        payment_method (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (PaymentMethodUpdateDescriptionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422
     """


    return sync_detailed(
        payment_method=payment_method,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    payment_method: str,
    *,
    client: AuthenticatedClient | Client,
    body: PaymentMethodUpdateDescriptionBody | Unset = UNSET,

) -> Response[PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422]:
    """ Update a payment method's description

     Sets a free-text description (max 100 characters, nullable) on the
    specified payment method. Only payment methods belonging to the
    authenticated main user may be updated. Returns the updated payment
    method. Main users only.

    Args:
        payment_method (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (PaymentMethodUpdateDescriptionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422]
     """


    kwargs = _get_kwargs(
        payment_method=payment_method,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    payment_method: str,
    *,
    client: AuthenticatedClient | Client,
    body: PaymentMethodUpdateDescriptionBody | Unset = UNSET,

) -> PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422 | None:
    """ Update a payment method's description

     Sets a free-text description (max 100 characters, nullable) on the
    specified payment method. Only payment methods belonging to the
    authenticated main user may be updated. Returns the updated payment
    method. Main users only.

    Args:
        payment_method (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (PaymentMethodUpdateDescriptionBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaymentMethodUpdateDescriptionResponse200 | PaymentMethodUpdateDescriptionResponse401 | PaymentMethodUpdateDescriptionResponse403 | PaymentMethodUpdateDescriptionResponse404 | PaymentMethodUpdateDescriptionResponse422
     """


    return (await asyncio_detailed(
        payment_method=payment_method,
client=client,
body=body,

    )).parsed
