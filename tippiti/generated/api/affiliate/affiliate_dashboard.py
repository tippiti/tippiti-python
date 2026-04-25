from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.affiliate_dashboard_response_200 import AffiliateDashboardResponse200
from ...models.affiliate_dashboard_response_401 import AffiliateDashboardResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AffiliateDashboardResponse200 | AffiliateDashboardResponse401 | None:
    if response.status_code == 200:
        response_200 = AffiliateDashboardResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AffiliateDashboardResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AffiliateDashboardResponse200 | AffiliateDashboardResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AffiliateDashboardResponse200 | AffiliateDashboardResponse401]:
    """ Get affiliate dashboard stats

     Returns aggregated partner-programme statistics for the authenticated
    account, including the referral code, current balance, lifetime totals
    and counts for clicks, sign-ups and confirmed commissions. Main users
    only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateDashboardResponse200 | AffiliateDashboardResponse401]
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

) -> AffiliateDashboardResponse200 | AffiliateDashboardResponse401 | None:
    """ Get affiliate dashboard stats

     Returns aggregated partner-programme statistics for the authenticated
    account, including the referral code, current balance, lifetime totals
    and counts for clicks, sign-ups and confirmed commissions. Main users
    only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateDashboardResponse200 | AffiliateDashboardResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AffiliateDashboardResponse200 | AffiliateDashboardResponse401]:
    """ Get affiliate dashboard stats

     Returns aggregated partner-programme statistics for the authenticated
    account, including the referral code, current balance, lifetime totals
    and counts for clicks, sign-ups and confirmed commissions. Main users
    only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateDashboardResponse200 | AffiliateDashboardResponse401]
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

) -> AffiliateDashboardResponse200 | AffiliateDashboardResponse401 | None:
    """ Get affiliate dashboard stats

     Returns aggregated partner-programme statistics for the authenticated
    account, including the referral code, current balance, lifetime totals
    and counts for clicks, sign-ups and confirmed commissions. Main users
    only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateDashboardResponse200 | AffiliateDashboardResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
