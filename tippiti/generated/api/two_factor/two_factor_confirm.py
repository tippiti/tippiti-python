from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.two_factor_confirm_body import TwoFactorConfirmBody
from ...models.two_factor_confirm_response_200 import TwoFactorConfirmResponse200
from ...models.two_factor_confirm_response_401 import TwoFactorConfirmResponse401
from ...models.two_factor_confirm_response_422 import TwoFactorConfirmResponse422
from typing import cast



def _get_kwargs(
    *,
    body: TwoFactorConfirmBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/two-factor/confirm",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422 | None:
    if response.status_code == 200:
        response_200 = TwoFactorConfirmResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = TwoFactorConfirmResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = TwoFactorConfirmResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwoFactorConfirmBody,

) -> Response[TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422]:
    """ Confirm two-factor enrolment

     Verifies the supplied TOTP `code` to finalise two-factor enrolment. On
    success two-factor becomes active and a set of one-time recovery codes
    is returned – these are shown only once and should be stored safely by
    the account holder.

    Args:
        body (TwoFactorConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422]
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
    body: TwoFactorConfirmBody,

) -> TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422 | None:
    """ Confirm two-factor enrolment

     Verifies the supplied TOTP `code` to finalise two-factor enrolment. On
    success two-factor becomes active and a set of one-time recovery codes
    is returned – these are shown only once and should be stored safely by
    the account holder.

    Args:
        body (TwoFactorConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TwoFactorConfirmBody,

) -> Response[TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422]:
    """ Confirm two-factor enrolment

     Verifies the supplied TOTP `code` to finalise two-factor enrolment. On
    success two-factor becomes active and a set of one-time recovery codes
    is returned – these are shown only once and should be stored safely by
    the account holder.

    Args:
        body (TwoFactorConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422]
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
    body: TwoFactorConfirmBody,

) -> TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422 | None:
    """ Confirm two-factor enrolment

     Verifies the supplied TOTP `code` to finalise two-factor enrolment. On
    success two-factor becomes active and a set of one-time recovery codes
    is returned – these are shown only once and should be stored safely by
    the account holder.

    Args:
        body (TwoFactorConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwoFactorConfirmResponse200 | TwoFactorConfirmResponse401 | TwoFactorConfirmResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
