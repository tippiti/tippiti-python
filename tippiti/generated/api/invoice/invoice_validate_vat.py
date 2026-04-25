from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_validate_vat_response_200_type_0 import InvoiceValidateVatResponse200Type0
from ...models.invoice_validate_vat_response_200_type_1 import InvoiceValidateVatResponse200Type1
from ...models.invoice_validate_vat_response_200_type_2 import InvoiceValidateVatResponse200Type2
from ...models.invoice_validate_vat_response_401 import InvoiceValidateVatResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing/invoices/validate-vat",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = InvoiceValidateVatResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = InvoiceValidateVatResponse200Type1.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = InvoiceValidateVatResponse200Type2.from_dict(data)



            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = InvoiceValidateVatResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401]:
    """ Validate the stored VAT ID

     Validates the VAT ID stored on the billing account's profile. If the
    VAT ID is found to be invalid it is removed from the profile and the
    response indicates the updated tax status and applicable tax rate.
    If no VAT ID is stored the response reflects that. Available to main
    users and to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401]
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

) -> InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401 | None:
    """ Validate the stored VAT ID

     Validates the VAT ID stored on the billing account's profile. If the
    VAT ID is found to be invalid it is removed from the profile and the
    response indicates the updated tax status and applicable tax rate.
    If no VAT ID is stored the response reflects that. Available to main
    users and to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401]:
    """ Validate the stored VAT ID

     Validates the VAT ID stored on the billing account's profile. If the
    VAT ID is found to be invalid it is removed from the profile and the
    response indicates the updated tax status and applicable tax rate.
    If no VAT ID is stored the response reflects that. Available to main
    users and to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401]
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

) -> InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401 | None:
    """ Validate the stored VAT ID

     Validates the VAT ID stored on the billing account's profile. If the
    VAT ID is found to be invalid it is removed from the profile and the
    response indicates the updated tax status and applicable tax rate.
    If no VAT ID is stored the response reflects that. Available to main
    users and to sub-users with billing access.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceValidateVatResponse200Type0 | InvoiceValidateVatResponse200Type1 | InvoiceValidateVatResponse200Type2 | InvoiceValidateVatResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
