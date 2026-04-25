from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_pay_body import InvoicePayBody
from ...models.invoice_pay_response_200_type_1 import InvoicePayResponse200Type1
from ...models.invoice_pay_response_401 import InvoicePayResponse401
from ...models.invoice_pay_response_403 import InvoicePayResponse403
from ...models.invoice_pay_response_404 import InvoicePayResponse404
from ...models.invoice_pay_response_409 import InvoicePayResponse409
from ...models.invoice_pay_response_422 import InvoicePayResponse422
from ...models.invoice_pay_response_500 import InvoicePayResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    invoice: str,
    *,
    body: InvoicePayBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing/invoices/{invoice}/pay".format(invoice=quote(str(invoice), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> InvoicePayResponse200Type1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = InvoicePayResponse200Type1.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvoicePayResponse200Type1 | str, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = InvoicePayResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InvoicePayResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = InvoicePayResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = InvoicePayResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = InvoicePayResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = InvoicePayResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500]:
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
    body: InvoicePayBody | Unset = UNSET,

) -> Response[InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500]:
    """ Pay an existing invoice

     Initiates payment for an unpaid invoice belonging to the billing
    account. Supported `mode` values are `saved_card` (default, requires
    `payment_method_id`), `checkout` and `paypal`. Concurrent requests
    against the same invoice return `409`. The response indicates success,
    further authentication required, or a redirect URL for hosted payment
    flows. Available to main users and to sub-users with billing access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (InvoicePayBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500]
     """


    kwargs = _get_kwargs(
        invoice=invoice,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    invoice: str,
    *,
    client: AuthenticatedClient | Client,
    body: InvoicePayBody | Unset = UNSET,

) -> InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500 | None:
    """ Pay an existing invoice

     Initiates payment for an unpaid invoice belonging to the billing
    account. Supported `mode` values are `saved_card` (default, requires
    `payment_method_id`), `checkout` and `paypal`. Concurrent requests
    against the same invoice return `409`. The response indicates success,
    further authentication required, or a redirect URL for hosted payment
    flows. Available to main users and to sub-users with billing access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (InvoicePayBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500
     """


    return sync_detailed(
        invoice=invoice,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    invoice: str,
    *,
    client: AuthenticatedClient | Client,
    body: InvoicePayBody | Unset = UNSET,

) -> Response[InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500]:
    """ Pay an existing invoice

     Initiates payment for an unpaid invoice belonging to the billing
    account. Supported `mode` values are `saved_card` (default, requires
    `payment_method_id`), `checkout` and `paypal`. Concurrent requests
    against the same invoice return `409`. The response indicates success,
    further authentication required, or a redirect URL for hosted payment
    flows. Available to main users and to sub-users with billing access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (InvoicePayBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500]
     """


    kwargs = _get_kwargs(
        invoice=invoice,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    invoice: str,
    *,
    client: AuthenticatedClient | Client,
    body: InvoicePayBody | Unset = UNSET,

) -> InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500 | None:
    """ Pay an existing invoice

     Initiates payment for an unpaid invoice belonging to the billing
    account. Supported `mode` values are `saved_card` (default, requires
    `payment_method_id`), `checkout` and `paypal`. Concurrent requests
    against the same invoice return `409`. The response indicates success,
    further authentication required, or a redirect URL for hosted payment
    flows. Available to main users and to sub-users with billing access.

    Args:
        invoice (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (InvoicePayBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoicePayResponse200Type1 | str | InvoicePayResponse401 | InvoicePayResponse403 | InvoicePayResponse404 | InvoicePayResponse409 | InvoicePayResponse422 | InvoicePayResponse500
     """


    return (await asyncio_detailed(
        invoice=invoice,
client=client,
body=body,

    )).parsed
