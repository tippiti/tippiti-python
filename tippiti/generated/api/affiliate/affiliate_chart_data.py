from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.affiliate_chart_data_period import AffiliateChartDataPeriod
from ...models.affiliate_chart_data_response_200 import AffiliateChartDataResponse200
from ...models.affiliate_chart_data_response_401 import AffiliateChartDataResponse401
from ...models.affiliate_chart_data_response_422 import AffiliateChartDataResponse422
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    period: AffiliateChartDataPeriod | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/affiliate/chart",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422 | None:
    if response.status_code == 200:
        response_200 = AffiliateChartDataResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AffiliateChartDataResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = AffiliateChartDataResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    period: AffiliateChartDataPeriod | Unset = UNSET,

) -> Response[AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422]:
    """ Get affiliate chart data

     Returns time-bucketed series for clicks, unique clicks, registrations
    and commission totals for the authenticated account. The optional
    `period` query parameter accepts `30d` (daily buckets), `1y` (weekly
    buckets) or `all` (monthly buckets) and defaults to `30d`. Main users
    only.

    Args:
        period (AffiliateChartDataPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422]
     """


    kwargs = _get_kwargs(
        period=period,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    period: AffiliateChartDataPeriod | Unset = UNSET,

) -> AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422 | None:
    """ Get affiliate chart data

     Returns time-bucketed series for clicks, unique clicks, registrations
    and commission totals for the authenticated account. The optional
    `period` query parameter accepts `30d` (daily buckets), `1y` (weekly
    buckets) or `all` (monthly buckets) and defaults to `30d`. Main users
    only.

    Args:
        period (AffiliateChartDataPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422
     """


    return sync_detailed(
        client=client,
period=period,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    period: AffiliateChartDataPeriod | Unset = UNSET,

) -> Response[AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422]:
    """ Get affiliate chart data

     Returns time-bucketed series for clicks, unique clicks, registrations
    and commission totals for the authenticated account. The optional
    `period` query parameter accepts `30d` (daily buckets), `1y` (weekly
    buckets) or `all` (monthly buckets) and defaults to `30d`. Main users
    only.

    Args:
        period (AffiliateChartDataPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422]
     """


    kwargs = _get_kwargs(
        period=period,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    period: AffiliateChartDataPeriod | Unset = UNSET,

) -> AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422 | None:
    """ Get affiliate chart data

     Returns time-bucketed series for clicks, unique clicks, registrations
    and commission totals for the authenticated account. The optional
    `period` query parameter accepts `30d` (daily buckets), `1y` (weekly
    buckets) or `all` (monthly buckets) and defaults to `30d`. Main users
    only.

    Args:
        period (AffiliateChartDataPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AffiliateChartDataResponse200 | AffiliateChartDataResponse401 | AffiliateChartDataResponse422
     """


    return (await asyncio_detailed(
        client=client,
period=period,

    )).parsed
