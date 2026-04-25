from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invoice_topup_response_200_type_1 import InvoiceTopupResponse200Type1
from ...models.invoice_topup_response_401 import InvoiceTopupResponse401
from ...models.invoice_topup_response_403 import InvoiceTopupResponse403
from ...models.invoice_topup_response_422 import InvoiceTopupResponse422
from ...models.invoice_topup_response_500 import InvoiceTopupResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/billing/invoices/topup",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> InvoiceTopupResponse200Type1 | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = InvoiceTopupResponse200Type1.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvoiceTopupResponse200Type1 | str, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = InvoiceTopupResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InvoiceTopupResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = InvoiceTopupResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = InvoiceTopupResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500]:
    """ Create and pay a top-up invoice

     Creates an invoice for the requested `amount` (in EUR, subject to the
    configured minimum) and immediately initiates payment. Supported
    `mode` values are `saved_card` (default, requires `payment_method_id`),
    `checkout` and `paypal`. The response indicates success, further
    authentication required, or a redirect URL for hosted payment flows.
    The billing profile must be complete. Available to main users and to
    sub-users with billing access.⚠️ Cannot generate request documentation: Cannot evaluate validation
    rules (1 evaluators failed):
      [NodeRulesEvaluator] Call to a member function getEffectiveUser() on null (at /var/www/app/app/ven
    dor/dedoc/scramble/src/Support/OperationExtensions/RulesEvaluator/NodeRulesEvaluator.php(199) :
    eval()'d code:3)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500]
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

) -> InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500 | None:
    """ Create and pay a top-up invoice

     Creates an invoice for the requested `amount` (in EUR, subject to the
    configured minimum) and immediately initiates payment. Supported
    `mode` values are `saved_card` (default, requires `payment_method_id`),
    `checkout` and `paypal`. The response indicates success, further
    authentication required, or a redirect URL for hosted payment flows.
    The billing profile must be complete. Available to main users and to
    sub-users with billing access.⚠️ Cannot generate request documentation: Cannot evaluate validation
    rules (1 evaluators failed):
      [NodeRulesEvaluator] Call to a member function getEffectiveUser() on null (at /var/www/app/app/ven
    dor/dedoc/scramble/src/Support/OperationExtensions/RulesEvaluator/NodeRulesEvaluator.php(199) :
    eval()'d code:3)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500]:
    """ Create and pay a top-up invoice

     Creates an invoice for the requested `amount` (in EUR, subject to the
    configured minimum) and immediately initiates payment. Supported
    `mode` values are `saved_card` (default, requires `payment_method_id`),
    `checkout` and `paypal`. The response indicates success, further
    authentication required, or a redirect URL for hosted payment flows.
    The billing profile must be complete. Available to main users and to
    sub-users with billing access.⚠️ Cannot generate request documentation: Cannot evaluate validation
    rules (1 evaluators failed):
      [NodeRulesEvaluator] Call to a member function getEffectiveUser() on null (at /var/www/app/app/ven
    dor/dedoc/scramble/src/Support/OperationExtensions/RulesEvaluator/NodeRulesEvaluator.php(199) :
    eval()'d code:3)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500]
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

) -> InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500 | None:
    """ Create and pay a top-up invoice

     Creates an invoice for the requested `amount` (in EUR, subject to the
    configured minimum) and immediately initiates payment. Supported
    `mode` values are `saved_card` (default, requires `payment_method_id`),
    `checkout` and `paypal`. The response indicates success, further
    authentication required, or a redirect URL for hosted payment flows.
    The billing profile must be complete. Available to main users and to
    sub-users with billing access.⚠️ Cannot generate request documentation: Cannot evaluate validation
    rules (1 evaluators failed):
      [NodeRulesEvaluator] Call to a member function getEffectiveUser() on null (at /var/www/app/app/ven
    dor/dedoc/scramble/src/Support/OperationExtensions/RulesEvaluator/NodeRulesEvaluator.php(199) :
    eval()'d code:3)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceTopupResponse200Type1 | str | InvoiceTopupResponse401 | InvoiceTopupResponse403 | InvoiceTopupResponse422 | InvoiceTopupResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
