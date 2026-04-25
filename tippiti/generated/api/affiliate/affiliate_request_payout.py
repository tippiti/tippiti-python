from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.affiliate_request_payout_body import AffiliateRequestPayoutBody
from ...models.affiliate_request_payout_response_201 import AffiliateRequestPayoutResponse201
from ...models.affiliate_request_payout_response_401 import AffiliateRequestPayoutResponse401
from ...models.affiliate_request_payout_response_422 import AffiliateRequestPayoutResponse422
from typing import cast



def _get_kwargs(
    *,
    body: AffiliateRequestPayoutBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/affiliate/payouts",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422 | None:
    if response.status_code == 201:
        response_201 = AffiliateRequestPayoutResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = AffiliateRequestPayoutResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = AffiliateRequestPayoutResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AffiliateRequestPayoutBody,

) -> Response[AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422]:
    """ Request a payout

     Submits a new payout request for the authenticated account's available
    commission balance. Requires `bank_holder` and a valid `bank_iban`;
    `bank_bic` is optional. The IBAN is normalised and checksum-validated
    (ISO 13616). The created payout is returned with its IBAN masked.
    Main users only.

    Args:
        body (AffiliateRequestPayoutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422]
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
    body: AffiliateRequestPayoutBody,

) -> AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422 | None:
    """ Request a payout

     Submits a new payout request for the authenticated account's available
    commission balance. Requires `bank_holder` and a valid `bank_iban`;
    `bank_bic` is optional. The IBAN is normalised and checksum-validated
    (ISO 13616). The created payout is returned with its IBAN masked.
    Main users only.

    Args:
        body (AffiliateRequestPayoutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AffiliateRequestPayoutBody,

) -> Response[AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422]:
    """ Request a payout

     Submits a new payout request for the authenticated account's available
    commission balance. Requires `bank_holder` and a valid `bank_iban`;
    `bank_bic` is optional. The IBAN is normalised and checksum-validated
    (ISO 13616). The created payout is returned with its IBAN masked.
    Main users only.

    Args:
        body (AffiliateRequestPayoutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422]
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
    body: AffiliateRequestPayoutBody,

) -> AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422 | None:
    """ Request a payout

     Submits a new payout request for the authenticated account's available
    commission balance. Requires `bank_holder` and a valid `bank_iban`;
    `bank_bic` is optional. The IBAN is normalised and checksum-validated
    (ISO 13616). The created payout is returned with its IBAN masked.
    Main users only.

    Args:
        body (AffiliateRequestPayoutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateRequestPayoutResponse201 | AffiliateRequestPayoutResponse401 | AffiliateRequestPayoutResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
