from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auth_login_response_200_type_0 import AuthLoginResponse200Type0
from ...models.auth_login_response_200_type_1 import AuthLoginResponse200Type1
from ...models.auth_login_response_422 import AuthLoginResponse422
from ...models.login_request import LoginRequest
from typing import cast



def _get_kwargs(
    *,
    body: LoginRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/login",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> AuthLoginResponse200Type0 | AuthLoginResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = AuthLoginResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = AuthLoginResponse200Type1.from_dict(data)



            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = AuthLoginResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoginRequest,

) -> Response[AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422]:
    """ Log in with email and password

     Authenticates the caller and returns the user together with a new API
    token on success. If the account has two-factor authentication enabled
    the response instead contains `two_factor_required: true` and a
    temporary `two_factor_token` that must be redeemed at the challenge
    endpoint to obtain a real API token. An optional `remember` flag
    requests a longer-lived token.

    Args:
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422]
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
    body: LoginRequest,

) -> AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422 | None:
    """ Log in with email and password

     Authenticates the caller and returns the user together with a new API
    token on success. If the account has two-factor authentication enabled
    the response instead contains `two_factor_required: true` and a
    temporary `two_factor_token` that must be redeemed at the challenge
    endpoint to obtain a real API token. An optional `remember` flag
    requests a longer-lived token.

    Args:
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LoginRequest,

) -> Response[AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422]:
    """ Log in with email and password

     Authenticates the caller and returns the user together with a new API
    token on success. If the account has two-factor authentication enabled
    the response instead contains `two_factor_required: true` and a
    temporary `two_factor_token` that must be redeemed at the challenge
    endpoint to obtain a real API token. An optional `remember` flag
    requests a longer-lived token.

    Args:
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422]
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
    body: LoginRequest,

) -> AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422 | None:
    """ Log in with email and password

     Authenticates the caller and returns the user together with a new API
    token on success. If the account has two-factor authentication enabled
    the response instead contains `two_factor_required: true` and a
    temporary `two_factor_token` that must be redeemed at the challenge
    endpoint to obtain a real API token. An optional `remember` flag
    requests a longer-lived token.

    Args:
        body (LoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthLoginResponse200Type0 | AuthLoginResponse200Type1 | AuthLoginResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
