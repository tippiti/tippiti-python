from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.sub_user_invite_response_200 import SubUserInviteResponse200
from ...models.sub_user_invite_response_401 import SubUserInviteResponse401
from ...models.sub_user_invite_response_404 import SubUserInviteResponse404
from typing import cast



def _get_kwargs(
    sub_user: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sub-users/{sub_user}/invite".format(sub_user=quote(str(sub_user), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404 | None:
    if response.status_code == 200:
        response_200 = SubUserInviteResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = SubUserInviteResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = SubUserInviteResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sub_user: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404]:
    """ Send a sub-user invitation email

     Sends an invitation email to a sub-user owned by the authenticated
    main user so the sub-user can set their password and activate the
    account. Main users only.

    Args:
        sub_user (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404]
     """


    kwargs = _get_kwargs(
        sub_user=sub_user,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    sub_user: str,
    *,
    client: AuthenticatedClient | Client,

) -> SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404 | None:
    """ Send a sub-user invitation email

     Sends an invitation email to a sub-user owned by the authenticated
    main user so the sub-user can set their password and activate the
    account. Main users only.

    Args:
        sub_user (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404
     """


    return sync_detailed(
        sub_user=sub_user,
client=client,

    ).parsed

async def asyncio_detailed(
    sub_user: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404]:
    """ Send a sub-user invitation email

     Sends an invitation email to a sub-user owned by the authenticated
    main user so the sub-user can set their password and activate the
    account. Main users only.

    Args:
        sub_user (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404]
     """


    kwargs = _get_kwargs(
        sub_user=sub_user,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    sub_user: str,
    *,
    client: AuthenticatedClient | Client,

) -> SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404 | None:
    """ Send a sub-user invitation email

     Sends an invitation email to a sub-user owned by the authenticated
    main user so the sub-user can set their password and activate the
    account. Main users only.

    Args:
        sub_user (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubUserInviteResponse200 | SubUserInviteResponse401 | SubUserInviteResponse404
     """


    return (await asyncio_detailed(
        sub_user=sub_user,
client=client,

    )).parsed
