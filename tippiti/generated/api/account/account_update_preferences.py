from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_update_preferences_body import AccountUpdatePreferencesBody
from ...models.account_update_preferences_response_200 import AccountUpdatePreferencesResponse200
from ...models.account_update_preferences_response_401 import AccountUpdatePreferencesResponse401
from ...models.account_update_preferences_response_403 import AccountUpdatePreferencesResponse403
from ...models.account_update_preferences_response_422 import AccountUpdatePreferencesResponse422
from typing import cast



def _get_kwargs(
    *,
    body: AccountUpdatePreferencesBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/account/preferences",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422 | None:
    if response.status_code == 200:
        response_200 = AccountUpdatePreferencesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountUpdatePreferencesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = AccountUpdatePreferencesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = AccountUpdatePreferencesResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AccountUpdatePreferencesBody,

) -> Response[AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422]:
    """ Store a UI preference

     Stores a single UI preference key/value for the authenticated account.
    Keys are lowercase alphanumeric (max 100 chars) and the value –
    serialised as JSON – must not exceed 2 KB. Keys that map to a gated
    behavior definition require the corresponding capability; others are
    rejected with `403`.

    Args:
        body (AccountUpdatePreferencesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422]
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
    body: AccountUpdatePreferencesBody,

) -> AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422 | None:
    """ Store a UI preference

     Stores a single UI preference key/value for the authenticated account.
    Keys are lowercase alphanumeric (max 100 chars) and the value –
    serialised as JSON – must not exceed 2 KB. Keys that map to a gated
    behavior definition require the corresponding capability; others are
    rejected with `403`.

    Args:
        body (AccountUpdatePreferencesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AccountUpdatePreferencesBody,

) -> Response[AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422]:
    """ Store a UI preference

     Stores a single UI preference key/value for the authenticated account.
    Keys are lowercase alphanumeric (max 100 chars) and the value –
    serialised as JSON – must not exceed 2 KB. Keys that map to a gated
    behavior definition require the corresponding capability; others are
    rejected with `403`.

    Args:
        body (AccountUpdatePreferencesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422]
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
    body: AccountUpdatePreferencesBody,

) -> AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422 | None:
    """ Store a UI preference

     Stores a single UI preference key/value for the authenticated account.
    Keys are lowercase alphanumeric (max 100 chars) and the value –
    serialised as JSON – must not exceed 2 KB. Keys that map to a gated
    behavior definition require the corresponding capability; others are
    rejected with `403`.

    Args:
        body (AccountUpdatePreferencesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountUpdatePreferencesResponse200 | AccountUpdatePreferencesResponse401 | AccountUpdatePreferencesResponse403 | AccountUpdatePreferencesResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
