from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.support_ticket_bulk_close_body import SupportTicketBulkCloseBody
from ...models.support_ticket_bulk_close_response_200 import SupportTicketBulkCloseResponse200
from ...models.support_ticket_bulk_close_response_401 import SupportTicketBulkCloseResponse401
from ...models.support_ticket_bulk_close_response_403 import SupportTicketBulkCloseResponse403
from ...models.support_ticket_bulk_close_response_422 import SupportTicketBulkCloseResponse422
from typing import cast



def _get_kwargs(
    *,
    body: SupportTicketBulkCloseBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/support/tickets/bulk/close",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422 | None:
    if response.status_code == 200:
        response_200 = SupportTicketBulkCloseResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = SupportTicketBulkCloseResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SupportTicketBulkCloseResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = SupportTicketBulkCloseResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SupportTicketBulkCloseBody,

) -> Response[SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422]:
    """ Close multiple support tickets

     Closes every ticket in the supplied `ids` list that the authenticated
    account is allowed to see; ids pointing to tickets outside that scope
    are ignored. Available to main users and to sub-users with the
    support-access capability.

    Args:
        body (SupportTicketBulkCloseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SupportTicketBulkCloseBody,

) -> SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422 | None:
    """ Close multiple support tickets

     Closes every ticket in the supplied `ids` list that the authenticated
    account is allowed to see; ids pointing to tickets outside that scope
    are ignored. Available to main users and to sub-users with the
    support-access capability.

    Args:
        body (SupportTicketBulkCloseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SupportTicketBulkCloseBody,

) -> Response[SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422]:
    """ Close multiple support tickets

     Closes every ticket in the supplied `ids` list that the authenticated
    account is allowed to see; ids pointing to tickets outside that scope
    are ignored. Available to main users and to sub-users with the
    support-access capability.

    Args:
        body (SupportTicketBulkCloseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SupportTicketBulkCloseBody,

) -> SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422 | None:
    """ Close multiple support tickets

     Closes every ticket in the supplied `ids` list that the authenticated
    account is allowed to see; ids pointing to tickets outside that scope
    are ignored. Available to main users and to sub-users with the
    support-access capability.

    Args:
        body (SupportTicketBulkCloseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportTicketBulkCloseResponse200 | SupportTicketBulkCloseResponse401 | SupportTicketBulkCloseResponse403 | SupportTicketBulkCloseResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
