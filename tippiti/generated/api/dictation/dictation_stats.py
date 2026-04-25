from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_stats_response_200 import DictationStatsResponse200
from ...models.dictation_stats_response_401 import DictationStatsResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dictations/stats",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationStatsResponse200 | DictationStatsResponse401 | None:
    if response.status_code == 200:
        response_200 = DictationStatsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationStatsResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationStatsResponse200 | DictationStatsResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationStatsResponse200 | DictationStatsResponse401]:
    """ Get dictation statistics for the current account

     Returns aggregate counts across the dictations visible to the caller:
    total number of dictations, number of completed dictations and total
    transcribed character count. The remaining character balance is
    included only when the caller has the balance-view capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationStatsResponse200 | DictationStatsResponse401]
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

) -> DictationStatsResponse200 | DictationStatsResponse401 | None:
    """ Get dictation statistics for the current account

     Returns aggregate counts across the dictations visible to the caller:
    total number of dictations, number of completed dictations and total
    transcribed character count. The remaining character balance is
    included only when the caller has the balance-view capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationStatsResponse200 | DictationStatsResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationStatsResponse200 | DictationStatsResponse401]:
    """ Get dictation statistics for the current account

     Returns aggregate counts across the dictations visible to the caller:
    total number of dictations, number of completed dictations and total
    transcribed character count. The remaining character balance is
    included only when the caller has the balance-view capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationStatsResponse200 | DictationStatsResponse401]
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

) -> DictationStatsResponse200 | DictationStatsResponse401 | None:
    """ Get dictation statistics for the current account

     Returns aggregate counts across the dictations visible to the caller:
    total number of dictations, number of completed dictations and total
    transcribed character count. The remaining character balance is
    included only when the caller has the balance-view capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationStatsResponse200 | DictationStatsResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
