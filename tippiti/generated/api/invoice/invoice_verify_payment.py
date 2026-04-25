from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_verify_payment_response_200_type_1 import InvoiceVerifyPaymentResponse200Type1
from ...models.invoice_verify_payment_response_401 import InvoiceVerifyPaymentResponse401
from ...models.invoice_verify_payment_response_403 import InvoiceVerifyPaymentResponse403
from ...models.invoice_verify_payment_response_404 import InvoiceVerifyPaymentResponse404
from typing import cast



def _get_kwargs(
    invoice: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing/invoices/{invoice}/verify-payment".format(invoice=quote(str(invoice), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> InvoiceVerifyPaymentResponse200Type1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = InvoiceVerifyPaymentResponse200Type1.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvoiceVerifyPaymentResponse200Type1 | str, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = InvoiceVerifyPaymentResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InvoiceVerifyPaymentResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = InvoiceVerifyPaymentResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404]:
    """ Verify a pending payment

     Reconciles the state of a payment that was initiated for the specified
    invoice – for example after returning from a hosted payment flow. The
    response reports whether the payment succeeded, is still pending or
    failed. Available to main users and to sub-users with billing access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404]
     """


    kwargs = _get_kwargs(
        invoice=invoice,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    invoice: str,
    *,
    client: AuthenticatedClient | Client,

) -> InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404 | None:
    """ Verify a pending payment

     Reconciles the state of a payment that was initiated for the specified
    invoice – for example after returning from a hosted payment flow. The
    response reports whether the payment succeeded, is still pending or
    failed. Available to main users and to sub-users with billing access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404
     """


    return sync_detailed(
        invoice=invoice,
client=client,

    ).parsed

async def asyncio_detailed(
    invoice: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404]:
    """ Verify a pending payment

     Reconciles the state of a payment that was initiated for the specified
    invoice – for example after returning from a hosted payment flow. The
    response reports whether the payment succeeded, is still pending or
    failed. Available to main users and to sub-users with billing access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404]
     """


    kwargs = _get_kwargs(
        invoice=invoice,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    invoice: str,
    *,
    client: AuthenticatedClient | Client,

) -> InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404 | None:
    """ Verify a pending payment

     Reconciles the state of a payment that was initiated for the specified
    invoice – for example after returning from a hosted payment flow. The
    response reports whether the payment succeeded, is still pending or
    failed. Available to main users and to sub-users with billing access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceVerifyPaymentResponse200Type1 | str | InvoiceVerifyPaymentResponse401 | InvoiceVerifyPaymentResponse403 | InvoiceVerifyPaymentResponse404
     """


    return (await asyncio_detailed(
        invoice=invoice,
client=client,

    )).parsed
