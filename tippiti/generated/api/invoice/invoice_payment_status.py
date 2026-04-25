from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_payment_status_response_200_type_0 import InvoicePaymentStatusResponse200Type0
from ...models.invoice_payment_status_response_200_type_1 import InvoicePaymentStatusResponse200Type1
from ...models.invoice_payment_status_response_200_type_2 import InvoicePaymentStatusResponse200Type2
from ...models.invoice_payment_status_response_200_type_3 import InvoicePaymentStatusResponse200Type3
from ...models.invoice_payment_status_response_401 import InvoicePaymentStatusResponse401
from ...models.invoice_payment_status_response_403 import InvoicePaymentStatusResponse403
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/billing/invoices/payment-status",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = InvoicePaymentStatusResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = InvoicePaymentStatusResponse200Type1.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = InvoicePaymentStatusResponse200Type2.from_dict(data)



                return response_200_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_3 = InvoicePaymentStatusResponse200Type3.from_dict(data)



            return response_200_type_3

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = InvoicePaymentStatusResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InvoicePaymentStatusResponse403.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403]:
    """ Get the latest payment status

     Returns the status of the most recent payment attempt for the billing
    account. The `status` is one of `none`, `pending`, `succeeded` or
    `failed`; on failure the response also contains a human-readable
    message. Available to main users and to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403]
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

) -> InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403 | None:
    """ Get the latest payment status

     Returns the status of the most recent payment attempt for the billing
    account. The `status` is one of `none`, `pending`, `succeeded` or
    `failed`; on failure the response also contains a human-readable
    message. Available to main users and to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403]:
    """ Get the latest payment status

     Returns the status of the most recent payment attempt for the billing
    account. The `status` is one of `none`, `pending`, `succeeded` or
    `failed`; on failure the response also contains a human-readable
    message. Available to main users and to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403]
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

) -> InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403 | None:
    """ Get the latest payment status

     Returns the status of the most recent payment attempt for the billing
    account. The `status` is one of `none`, `pending`, `succeeded` or
    `failed`; on failure the response also contains a human-readable
    message. Available to main users and to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicePaymentStatusResponse200Type0 | InvoicePaymentStatusResponse200Type1 | InvoicePaymentStatusResponse200Type2 | InvoicePaymentStatusResponse200Type3 | InvoicePaymentStatusResponse401 | InvoicePaymentStatusResponse403
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
