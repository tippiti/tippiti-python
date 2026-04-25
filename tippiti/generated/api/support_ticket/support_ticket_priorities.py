from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.support_ticket_priorities_response_200 import SupportTicketPrioritiesResponse200
from ...models.support_ticket_priorities_response_401 import SupportTicketPrioritiesResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/support/priorities",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401 | None:
    if response.status_code == 200:
        response_200 = SupportTicketPrioritiesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = SupportTicketPrioritiesResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401]:
    """ List ticket priorities

     Returns the active support ticket priorities that can be selected when
    opening a ticket, with the default priority flagged. Available to main
    users and to sub-users with the support-access capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401]
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

) -> SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401 | None:
    """ List ticket priorities

     Returns the active support ticket priorities that can be selected when
    opening a ticket, with the default priority flagged. Available to main
    users and to sub-users with the support-access capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401]:
    """ List ticket priorities

     Returns the active support ticket priorities that can be selected when
    opening a ticket, with the default priority flagged. Available to main
    users and to sub-users with the support-access capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401]
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

) -> SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401 | None:
    """ List ticket priorities

     Returns the active support ticket priorities that can be selected when
    opening a ticket, with the default priority flagged. Available to main
    users and to sub-users with the support-access capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketPrioritiesResponse200 | SupportTicketPrioritiesResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
