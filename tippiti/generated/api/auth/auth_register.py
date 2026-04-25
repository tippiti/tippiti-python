from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auth_register_response_201 import AuthRegisterResponse201
from ...models.auth_register_response_422 import AuthRegisterResponse422
from ...models.register_request import RegisterRequest
from typing import cast



def _get_kwargs(
    *,
    body: RegisterRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/register",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthRegisterResponse201 | AuthRegisterResponse422 | None:
    if response.status_code == 201:
        response_201 = AuthRegisterResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 422:
        response_422 = AuthRegisterResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthRegisterResponse201 | AuthRegisterResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RegisterRequest,

) -> Response[AuthRegisterResponse201 | AuthRegisterResponse422]:
    """ Register a new account

     Creates a new main user account and returns the user record together
    with an API token. A verification email is sent to the supplied address;
    the account is considered verified once the link is confirmed. An
    optional `referral_code` may be supplied to associate the account with
    a partner code.

    Args:
        body (RegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthRegisterResponse201 | AuthRegisterResponse422]
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
    body: RegisterRequest,

) -> AuthRegisterResponse201 | AuthRegisterResponse422 | None:
    """ Register a new account

     Creates a new main user account and returns the user record together
    with an API token. A verification email is sent to the supplied address;
    the account is considered verified once the link is confirmed. An
    optional `referral_code` may be supplied to associate the account with
    a partner code.

    Args:
        body (RegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthRegisterResponse201 | AuthRegisterResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RegisterRequest,

) -> Response[AuthRegisterResponse201 | AuthRegisterResponse422]:
    """ Register a new account

     Creates a new main user account and returns the user record together
    with an API token. A verification email is sent to the supplied address;
    the account is considered verified once the link is confirmed. An
    optional `referral_code` may be supplied to associate the account with
    a partner code.

    Args:
        body (RegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthRegisterResponse201 | AuthRegisterResponse422]
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
    body: RegisterRequest,

) -> AuthRegisterResponse201 | AuthRegisterResponse422 | None:
    """ Register a new account

     Creates a new main user account and returns the user record together
    with an API token. A verification email is sent to the supplied address;
    the account is considered verified once the link is confirmed. An
    optional `referral_code` may be supplied to associate the account with
    a partner code.

    Args:
        body (RegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthRegisterResponse201 | AuthRegisterResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
