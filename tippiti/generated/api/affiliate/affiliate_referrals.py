from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.affiliate_referrals_response_200 import AffiliateReferralsResponse200
from ...models.affiliate_referrals_response_401 import AffiliateReferralsResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate/referrals",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AffiliateReferralsResponse200 | AffiliateReferralsResponse401 | None:
    if response.status_code == 200:
        response_200 = AffiliateReferralsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AffiliateReferralsResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AffiliateReferralsResponse200 | AffiliateReferralsResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AffiliateReferralsResponse200 | AffiliateReferralsResponse401]:
    """ List referred accounts

     Returns accounts that signed up via the authenticated account's
    referral code. Each entry includes the referral date, whether the
    referred account is currently active, and totals for confirmed and
    pending commissions earned from that referral. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateReferralsResponse200 | AffiliateReferralsResponse401]
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

) -> AffiliateReferralsResponse200 | AffiliateReferralsResponse401 | None:
    """ List referred accounts

     Returns accounts that signed up via the authenticated account's
    referral code. Each entry includes the referral date, whether the
    referred account is currently active, and totals for confirmed and
    pending commissions earned from that referral. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateReferralsResponse200 | AffiliateReferralsResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AffiliateReferralsResponse200 | AffiliateReferralsResponse401]:
    """ List referred accounts

     Returns accounts that signed up via the authenticated account's
    referral code. Each entry includes the referral date, whether the
    referred account is currently active, and totals for confirmed and
    pending commissions earned from that referral. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateReferralsResponse200 | AffiliateReferralsResponse401]
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

) -> AffiliateReferralsResponse200 | AffiliateReferralsResponse401 | None:
    """ List referred accounts

     Returns accounts that signed up via the authenticated account's
    referral code. Each entry includes the referral date, whether the
    referred account is currently active, and totals for confirmed and
    pending commissions earned from that referral. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateReferralsResponse200 | AffiliateReferralsResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
