from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auto_topup_show_response_200 import AutoTopupShowResponse200
from ...models.auto_topup_show_response_401 import AutoTopupShowResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/billing/auto-topup",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AutoTopupShowResponse200 | AutoTopupShowResponse401 | None:
    if response.status_code == 200:
        response_200 = AutoTopupShowResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AutoTopupShowResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AutoTopupShowResponse200 | AutoTopupShowResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AutoTopupShowResponse200 | AutoTopupShowResponse401]:
    """ Get auto top-up settings

     Returns the current auto top-up configuration for the authenticated
    main user: whether it is enabled, the balance threshold that triggers
    a top-up, the top-up amount, the selected payment method and the
    minimum allowed top-up amount. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoTopupShowResponse200 | AutoTopupShowResponse401]
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

) -> AutoTopupShowResponse200 | AutoTopupShowResponse401 | None:
    """ Get auto top-up settings

     Returns the current auto top-up configuration for the authenticated
    main user: whether it is enabled, the balance threshold that triggers
    a top-up, the top-up amount, the selected payment method and the
    minimum allowed top-up amount. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoTopupShowResponse200 | AutoTopupShowResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AutoTopupShowResponse200 | AutoTopupShowResponse401]:
    """ Get auto top-up settings

     Returns the current auto top-up configuration for the authenticated
    main user: whether it is enabled, the balance threshold that triggers
    a top-up, the top-up amount, the selected payment method and the
    minimum allowed top-up amount. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoTopupShowResponse200 | AutoTopupShowResponse401]
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

) -> AutoTopupShowResponse200 | AutoTopupShowResponse401 | None:
    """ Get auto top-up settings

     Returns the current auto top-up configuration for the authenticated
    main user: whether it is enabled, the balance threshold that triggers
    a top-up, the top-up amount, the selected payment method and the
    minimum allowed top-up amount. Main users only.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoTopupShowResponse200 | AutoTopupShowResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
