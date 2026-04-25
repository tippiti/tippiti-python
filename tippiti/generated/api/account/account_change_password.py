from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_change_password_response_200 import AccountChangePasswordResponse200
from ...models.account_change_password_response_401 import AccountChangePasswordResponse401
from ...models.account_change_password_response_422 import AccountChangePasswordResponse422
from ...models.change_password_request import ChangePasswordRequest
from typing import cast



def _get_kwargs(
    *,
    body: ChangePasswordRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/account/password",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422 | None:
    if response.status_code == 200:
        response_200 = AccountChangePasswordResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountChangePasswordResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = AccountChangePasswordResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ChangePasswordRequest,

) -> Response[AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422]:
    """ Change account password

     Changes the authenticated account's password. The current password
    must be supplied and is verified server-side. On success all other
    access tokens are revoked – only the token used for this request
    remains valid.

    Args:
        body (ChangePasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422]
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
    body: ChangePasswordRequest,

) -> AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422 | None:
    """ Change account password

     Changes the authenticated account's password. The current password
    must be supplied and is verified server-side. On success all other
    access tokens are revoked – only the token used for this request
    remains valid.

    Args:
        body (ChangePasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ChangePasswordRequest,

) -> Response[AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422]:
    """ Change account password

     Changes the authenticated account's password. The current password
    must be supplied and is verified server-side. On success all other
    access tokens are revoked – only the token used for this request
    remains valid.

    Args:
        body (ChangePasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422]
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
    body: ChangePasswordRequest,

) -> AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422 | None:
    """ Change account password

     Changes the authenticated account's password. The current password
    must be supplied and is verified server-side. On success all other
    access tokens are revoked – only the token used for this request
    remains valid.

    Args:
        body (ChangePasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountChangePasswordResponse200 | AccountChangePasswordResponse401 | AccountChangePasswordResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
