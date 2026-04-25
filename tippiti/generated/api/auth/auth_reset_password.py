from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auth_reset_password_body import AuthResetPasswordBody
from ...models.auth_reset_password_response_200 import AuthResetPasswordResponse200
from ...models.auth_reset_password_response_422 import AuthResetPasswordResponse422
from typing import cast



def _get_kwargs(
    *,
    body: AuthResetPasswordBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/reset-password",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthResetPasswordResponse200 | AuthResetPasswordResponse422 | None:
    if response.status_code == 200:
        response_200 = AuthResetPasswordResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = AuthResetPasswordResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthResetPasswordResponse200 | AuthResetPasswordResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthResetPasswordBody,

) -> Response[AuthResetPasswordResponse200 | AuthResetPasswordResponse422]:
    """ Reset the password using a token

     Sets a new password using the signed token received by email. The
    supplied `password` must be at least 8 characters and match
    `password_confirmation`. On success all existing API tokens for the
    account are revoked. Invalid or expired tokens return a validation
    error.

    Args:
        body (AuthResetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthResetPasswordResponse200 | AuthResetPasswordResponse422]
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
    body: AuthResetPasswordBody,

) -> AuthResetPasswordResponse200 | AuthResetPasswordResponse422 | None:
    """ Reset the password using a token

     Sets a new password using the signed token received by email. The
    supplied `password` must be at least 8 characters and match
    `password_confirmation`. On success all existing API tokens for the
    account are revoked. Invalid or expired tokens return a validation
    error.

    Args:
        body (AuthResetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthResetPasswordResponse200 | AuthResetPasswordResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthResetPasswordBody,

) -> Response[AuthResetPasswordResponse200 | AuthResetPasswordResponse422]:
    """ Reset the password using a token

     Sets a new password using the signed token received by email. The
    supplied `password` must be at least 8 characters and match
    `password_confirmation`. On success all existing API tokens for the
    account are revoked. Invalid or expired tokens return a validation
    error.

    Args:
        body (AuthResetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthResetPasswordResponse200 | AuthResetPasswordResponse422]
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
    body: AuthResetPasswordBody,

) -> AuthResetPasswordResponse200 | AuthResetPasswordResponse422 | None:
    """ Reset the password using a token

     Sets a new password using the signed token received by email. The
    supplied `password` must be at least 8 characters and match
    `password_confirmation`. On success all existing API tokens for the
    account are revoked. Invalid or expired tokens return a validation
    error.

    Args:
        body (AuthResetPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthResetPasswordResponse200 | AuthResetPasswordResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
