from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_download_pdf_response_401 import InvoiceDownloadPdfResponse401
from ...models.invoice_download_pdf_response_403 import InvoiceDownloadPdfResponse403
from ...models.invoice_download_pdf_response_404 import InvoiceDownloadPdfResponse404
from typing import cast



def _get_kwargs(
    invoice: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/billing/invoices/{invoice}/pdf".format(invoice=quote(str(invoice), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 401:
        response_401 = InvoiceDownloadPdfResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InvoiceDownloadPdfResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = InvoiceDownloadPdfResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str]:
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

) -> Response[InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str]:
    """ Download an invoice as PDF

     Streams the specified invoice as a PDF attachment. The filename is the
    invoice number. Only invoices belonging to the billing account may be
    downloaded. Available to main users and to sub-users with billing
    access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str]
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

) -> InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str | None:
    """ Download an invoice as PDF

     Streams the specified invoice as a PDF attachment. The filename is the
    invoice number. Only invoices belonging to the billing account may be
    downloaded. Available to main users and to sub-users with billing
    access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str
     """


    return sync_detailed(
        invoice=invoice,
client=client,

    ).parsed

async def asyncio_detailed(
    invoice: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str]:
    """ Download an invoice as PDF

     Streams the specified invoice as a PDF attachment. The filename is the
    invoice number. Only invoices belonging to the billing account may be
    downloaded. Available to main users and to sub-users with billing
    access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str]
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

) -> InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str | None:
    """ Download an invoice as PDF

     Streams the specified invoice as a PDF attachment. The filename is the
    invoice number. Only invoices belonging to the billing account may be
    downloaded. Available to main users and to sub-users with billing
    access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceDownloadPdfResponse401 | InvoiceDownloadPdfResponse403 | InvoiceDownloadPdfResponse404 | str
     """


    return (await asyncio_detailed(
        invoice=invoice,
client=client,

    )).parsed
