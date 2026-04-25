from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.support_ticket_index_response_200 import SupportTicketIndexResponse200
from ...models.support_ticket_index_response_401 import SupportTicketIndexResponse401
from ...models.support_ticket_index_response_403 import SupportTicketIndexResponse403
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/support/tickets",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403 | None:
    if response.status_code == 200:
        response_200 = SupportTicketIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = SupportTicketIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SupportTicketIndexResponse403.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403]:
    """ List support tickets

     Returns the support tickets visible to the authenticated account. Main
    users see their own tickets plus those of their sub-users; sub-users
    see their own tickets and their parent account's tickets. Requires the
    support-access capability for sub-users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403]
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

) -> SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403 | None:
    """ List support tickets

     Returns the support tickets visible to the authenticated account. Main
    users see their own tickets plus those of their sub-users; sub-users
    see their own tickets and their parent account's tickets. Requires the
    support-access capability for sub-users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403]:
    """ List support tickets

     Returns the support tickets visible to the authenticated account. Main
    users see their own tickets plus those of their sub-users; sub-users
    see their own tickets and their parent account's tickets. Requires the
    support-access capability for sub-users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403]
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

) -> SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403 | None:
    """ List support tickets

     Returns the support tickets visible to the authenticated account. Main
    users see their own tickets plus those of their sub-users; sub-users
    see their own tickets and their parent account's tickets. Requires the
    support-access capability for sub-users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketIndexResponse200 | SupportTicketIndexResponse401 | SupportTicketIndexResponse403
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
