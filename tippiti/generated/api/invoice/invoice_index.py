from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_index_response_200 import InvoiceIndexResponse200
from ...models.invoice_index_response_401 import InvoiceIndexResponse401
from ...models.invoice_index_response_403 import InvoiceIndexResponse403
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/billing/invoices",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403 | None:
    if response.status_code == 200:
        response_200 = InvoiceIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = InvoiceIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InvoiceIndexResponse403.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403]:
    """ List invoices

     Returns all pending and paid invoices for the billing account in
    reverse chronological order. Each entry includes the invoice number,
    totals, tax breakdown, currency and status. Available to main users
    and to sub-users with billing access; in both cases the main account's
    invoices are returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403]
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

) -> InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403 | None:
    """ List invoices

     Returns all pending and paid invoices for the billing account in
    reverse chronological order. Each entry includes the invoice number,
    totals, tax breakdown, currency and status. Available to main users
    and to sub-users with billing access; in both cases the main account's
    invoices are returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403]:
    """ List invoices

     Returns all pending and paid invoices for the billing account in
    reverse chronological order. Each entry includes the invoice number,
    totals, tax breakdown, currency and status. Available to main users
    and to sub-users with billing access; in both cases the main account's
    invoices are returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403]
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

) -> InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403 | None:
    """ List invoices

     Returns all pending and paid invoices for the billing account in
    reverse chronological order. Each entry includes the invoice number,
    totals, tax breakdown, currency and status. Available to main users
    and to sub-users with billing access; in both cases the main account's
    invoices are returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceIndexResponse200 | InvoiceIndexResponse401 | InvoiceIndexResponse403
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
