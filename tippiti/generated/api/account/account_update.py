from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_update_response_200 import AccountUpdateResponse200
from ...models.account_update_response_401 import AccountUpdateResponse401
from ...models.account_update_response_422 import AccountUpdateResponse422
from ...models.update_account_request import UpdateAccountRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UpdateAccountRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/account",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = AccountUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AccountUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = AccountUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAccountRequest | Unset = UNSET,

) -> Response[AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422]:
    """ Update account profile

     Updates the authenticated account's profile. Main users may update
    billing details (company, address, tax ID); sub-users cannot change
    these fields. A supplied `tax_id` must be a valid EU VAT identifier.
    Changing `email` invalidates the previous verification and triggers a
    new verification email.

    Args:
        body (UpdateAccountRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422]
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
    body: UpdateAccountRequest | Unset = UNSET,

) -> AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422 | None:
    """ Update account profile

     Updates the authenticated account's profile. Main users may update
    billing details (company, address, tax ID); sub-users cannot change
    these fields. A supplied `tax_id` must be a valid EU VAT identifier.
    Changing `email` invalidates the previous verification and triggers a
    new verification email.

    Args:
        body (UpdateAccountRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAccountRequest | Unset = UNSET,

) -> Response[AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422]:
    """ Update account profile

     Updates the authenticated account's profile. Main users may update
    billing details (company, address, tax ID); sub-users cannot change
    these fields. A supplied `tax_id` must be a valid EU VAT identifier.
    Changing `email` invalidates the previous verification and triggers a
    new verification email.

    Args:
        body (UpdateAccountRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422]
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
    body: UpdateAccountRequest | Unset = UNSET,

) -> AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422 | None:
    """ Update account profile

     Updates the authenticated account's profile. Main users may update
    billing details (company, address, tax ID); sub-users cannot change
    these fields. A supplied `tax_id` must be a valid EU VAT identifier.
    Changing `email` invalidates the previous verification and triggers a
    new verification email.

    Args:
        body (UpdateAccountRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountUpdateResponse200 | AccountUpdateResponse401 | AccountUpdateResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
