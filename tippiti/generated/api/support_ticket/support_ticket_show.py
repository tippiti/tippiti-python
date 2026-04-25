from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.support_ticket_show_response_200 import SupportTicketShowResponse200
from ...models.support_ticket_show_response_401 import SupportTicketShowResponse401
from ...models.support_ticket_show_response_403 import SupportTicketShowResponse403
from ...models.support_ticket_show_response_404 import SupportTicketShowResponse404
from typing import cast



def _get_kwargs(
    ticket: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/support/tickets/{ticket}".format(ticket=quote(str(ticket), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404 | None:
    if response.status_code == 200:
        response_200 = SupportTicketShowResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = SupportTicketShowResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SupportTicketShowResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SupportTicketShowResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ticket: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404]:
    """ Get a support ticket

     Returns a single support ticket together with its public replies and
    their attachments, if the authenticated account is allowed to view it.
    Available to main users and to sub-users with the support-access
    capability.

    Args:
        ticket (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404]
     """


    kwargs = _get_kwargs(
        ticket=ticket,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    ticket: str,
    *,
    client: AuthenticatedClient | Client,

) -> SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404 | None:
    """ Get a support ticket

     Returns a single support ticket together with its public replies and
    their attachments, if the authenticated account is allowed to view it.
    Available to main users and to sub-users with the support-access
    capability.

    Args:
        ticket (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404
     """


    return sync_detailed(
        ticket=ticket,
client=client,

    ).parsed

async def asyncio_detailed(
    ticket: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404]:
    """ Get a support ticket

     Returns a single support ticket together with its public replies and
    their attachments, if the authenticated account is allowed to view it.
    Available to main users and to sub-users with the support-access
    capability.

    Args:
        ticket (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404]
     """


    kwargs = _get_kwargs(
        ticket=ticket,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ticket: str,
    *,
    client: AuthenticatedClient | Client,

) -> SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404 | None:
    """ Get a support ticket

     Returns a single support ticket together with its public replies and
    their attachments, if the authenticated account is allowed to view it.
    Available to main users and to sub-users with the support-access
    capability.

    Args:
        ticket (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketShowResponse200 | SupportTicketShowResponse401 | SupportTicketShowResponse403 | SupportTicketShowResponse404
     """


    return (await asyncio_detailed(
        ticket=ticket,
client=client,

    )).parsed
