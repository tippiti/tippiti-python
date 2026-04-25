from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.two_factor_enable_response_200 import TwoFactorEnableResponse200
from ...models.two_factor_enable_response_401 import TwoFactorEnableResponse401
from ...models.two_factor_enable_response_422 import TwoFactorEnableResponse422
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/two-factor/enable",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422 | None:
    if response.status_code == 200:
        response_200 = TwoFactorEnableResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = TwoFactorEnableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = TwoFactorEnableResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422]:
    """ Start two-factor enrolment

     Generates a TOTP secret for the authenticated account and returns it
    together with an otpauth-style QR code URL that can be scanned by any
    standard authenticator app. Two-factor is not yet active – call the
    confirm endpoint with a valid TOTP code to finalise enrolment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422]
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

) -> TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422 | None:
    """ Start two-factor enrolment

     Generates a TOTP secret for the authenticated account and returns it
    together with an otpauth-style QR code URL that can be scanned by any
    standard authenticator app. Two-factor is not yet active – call the
    confirm endpoint with a valid TOTP code to finalise enrolment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422]:
    """ Start two-factor enrolment

     Generates a TOTP secret for the authenticated account and returns it
    together with an otpauth-style QR code URL that can be scanned by any
    standard authenticator app. Two-factor is not yet active – call the
    confirm endpoint with a valid TOTP code to finalise enrolment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422]
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

) -> TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422 | None:
    """ Start two-factor enrolment

     Generates a TOTP secret for the authenticated account and returns it
    together with an otpauth-style QR code URL that can be scanned by any
    standard authenticator app. Two-factor is not yet active – call the
    confirm endpoint with a valid TOTP code to finalise enrolment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TwoFactorEnableResponse200 | TwoFactorEnableResponse401 | TwoFactorEnableResponse422
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
