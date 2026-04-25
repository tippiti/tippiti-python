from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.store_support_ticket_reply_request import StoreSupportTicketReplyRequest
from ...models.support_ticket_reply_response_200 import SupportTicketReplyResponse200
from ...models.support_ticket_reply_response_401 import SupportTicketReplyResponse401
from ...models.support_ticket_reply_response_403 import SupportTicketReplyResponse403
from ...models.support_ticket_reply_response_404 import SupportTicketReplyResponse404
from ...models.support_ticket_reply_response_422 import SupportTicketReplyResponse422
from typing import cast



def _get_kwargs(
    ticket: str,
    *,
    body: StoreSupportTicketReplyRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/support/tickets/{ticket}/replies".format(ticket=quote(str(ticket), safe=""),),
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422 | None:
    if response.status_code == 200:
        response_200 = SupportTicketReplyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = SupportTicketReplyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SupportTicketReplyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SupportTicketReplyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = SupportTicketReplyResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422]:
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
    body: StoreSupportTicketReplyRequest,

) -> Response[SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422]:
    """ Reply to a support ticket

     Appends a customer reply – with optional file attachments – to an
    existing ticket. If the ticket was closed it is reopened. Available to
    main users and to sub-users with the support-access capability.

    Args:
        ticket (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (StoreSupportTicketReplyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422]
     """


    kwargs = _get_kwargs(
        ticket=ticket,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    ticket: str,
    *,
    client: AuthenticatedClient | Client,
    body: StoreSupportTicketReplyRequest,

) -> SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422 | None:
    """ Reply to a support ticket

     Appends a customer reply – with optional file attachments – to an
    existing ticket. If the ticket was closed it is reopened. Available to
    main users and to sub-users with the support-access capability.

    Args:
        ticket (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (StoreSupportTicketReplyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422
     """


    return sync_detailed(
        ticket=ticket,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    ticket: str,
    *,
    client: AuthenticatedClient | Client,
    body: StoreSupportTicketReplyRequest,

) -> Response[SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422]:
    """ Reply to a support ticket

     Appends a customer reply – with optional file attachments – to an
    existing ticket. If the ticket was closed it is reopened. Available to
    main users and to sub-users with the support-access capability.

    Args:
        ticket (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (StoreSupportTicketReplyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422]
     """


    kwargs = _get_kwargs(
        ticket=ticket,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ticket: str,
    *,
    client: AuthenticatedClient | Client,
    body: StoreSupportTicketReplyRequest,

) -> SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422 | None:
    """ Reply to a support ticket

     Appends a customer reply – with optional file attachments – to an
    existing ticket. If the ticket was closed it is reopened. Available to
    main users and to sub-users with the support-access capability.

    Args:
        ticket (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (StoreSupportTicketReplyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketReplyResponse200 | SupportTicketReplyResponse401 | SupportTicketReplyResponse403 | SupportTicketReplyResponse404 | SupportTicketReplyResponse422
     """


    return (await asyncio_detailed(
        ticket=ticket,
client=client,
body=body,

    )).parsed
