from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.two_factor_recovery_codes_body import TwoFactorRecoveryCodesBody
from ...models.two_factor_recovery_codes_response_200 import TwoFactorRecoveryCodesResponse200
from ...models.two_factor_recovery_codes_response_401 import TwoFactorRecoveryCodesResponse401
from ...models.two_factor_recovery_codes_response_422 import TwoFactorRecoveryCodesResponse422
from typing import cast



def _get_kwargs(
    *,
    body: TwoFactorRecoveryCodesBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/two-factor/recovery-codes",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422 | None:
    if response.status_code == 200:
        response_200 = TwoFactorRecoveryCodesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = TwoFactorRecoveryCodesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = TwoFactorRecoveryCodesResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwoFactorRecoveryCodesBody,

) -> Response[TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422]:
    """ Regenerate recovery codes

     Replaces the authenticated account's two-factor recovery codes with a
    fresh set and returns them. Any previously issued recovery codes are
    invalidated. The current account `password` must be supplied for
    confirmation.

    Args:
        body (TwoFactorRecoveryCodesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422]
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
    body: TwoFactorRecoveryCodesBody,

) -> TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422 | None:
    """ Regenerate recovery codes

     Replaces the authenticated account's two-factor recovery codes with a
    fresh set and returns them. Any previously issued recovery codes are
    invalidated. The current account `password` must be supplied for
    confirmation.

    Args:
        body (TwoFactorRecoveryCodesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwoFactorRecoveryCodesBody,

) -> Response[TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422]:
    """ Regenerate recovery codes

     Replaces the authenticated account's two-factor recovery codes with a
    fresh set and returns them. Any previously issued recovery codes are
    invalidated. The current account `password` must be supplied for
    confirmation.

    Args:
        body (TwoFactorRecoveryCodesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422]
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
    body: TwoFactorRecoveryCodesBody,

) -> TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422 | None:
    """ Regenerate recovery codes

     Replaces the authenticated account's two-factor recovery codes with a
    fresh set and returns them. Any previously issued recovery codes are
    invalidated. The current account `password` must be supplied for
    confirmation.

    Args:
        body (TwoFactorRecoveryCodesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwoFactorRecoveryCodesResponse200 | TwoFactorRecoveryCodesResponse401 | TwoFactorRecoveryCodesResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
