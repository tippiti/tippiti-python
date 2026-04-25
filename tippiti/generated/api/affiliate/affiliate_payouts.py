from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.affiliate_payouts_response_200 import AffiliatePayoutsResponse200
from ...models.affiliate_payouts_response_401 import AffiliatePayoutsResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate/payouts",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401 | None:
    if response.status_code == 200:
        response_200 = AffiliatePayoutsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AffiliatePayoutsResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401]:
    """ List affiliate payouts

     Returns the authenticated account's payout requests in reverse
    chronological order. Each entry includes amount, status, account
    holder, masked IBAN, request and payment timestamps, and – when
    rejected – the rejection reason. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401]
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

) -> AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401 | None:
    """ List affiliate payouts

     Returns the authenticated account's payout requests in reverse
    chronological order. Each entry includes amount, status, account
    holder, masked IBAN, request and payment timestamps, and – when
    rejected – the rejection reason. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401]:
    """ List affiliate payouts

     Returns the authenticated account's payout requests in reverse
    chronological order. Each entry includes amount, status, account
    holder, masked IBAN, request and payment timestamps, and – when
    rejected – the rejection reason. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401]
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

) -> AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401 | None:
    """ List affiliate payouts

     Returns the authenticated account's payout requests in reverse
    chronological order. Each entry includes amount, status, account
    holder, masked IBAN, request and payment timestamps, and – when
    rejected – the rejection reason. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliatePayoutsResponse200 | AffiliatePayoutsResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
