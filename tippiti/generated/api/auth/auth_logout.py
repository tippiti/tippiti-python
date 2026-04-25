from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auth_logout_response_200 import AuthLogoutResponse200
from ...models.auth_logout_response_401 import AuthLogoutResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/logout",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthLogoutResponse200 | AuthLogoutResponse401 | None:
    if response.status_code == 200:
        response_200 = AuthLogoutResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AuthLogoutResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthLogoutResponse200 | AuthLogoutResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AuthLogoutResponse200 | AuthLogoutResponse401]:
    """ Log out the current session

     Revokes the API token used for this request. Other tokens issued to
    the same account remain valid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthLogoutResponse200 | AuthLogoutResponse401]
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

) -> AuthLogoutResponse200 | AuthLogoutResponse401 | None:
    """ Log out the current session

     Revokes the API token used for this request. Other tokens issued to
    the same account remain valid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthLogoutResponse200 | AuthLogoutResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AuthLogoutResponse200 | AuthLogoutResponse401]:
    """ Log out the current session

     Revokes the API token used for this request. Other tokens issued to
    the same account remain valid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthLogoutResponse200 | AuthLogoutResponse401]
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

) -> AuthLogoutResponse200 | AuthLogoutResponse401 | None:
    """ Log out the current session

     Revokes the API token used for this request. Other tokens issued to
    the same account remain valid.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthLogoutResponse200 | AuthLogoutResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
