from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.email_verification_resend_response_200_type_0 import EmailVerificationResendResponse200Type0
from ...models.email_verification_resend_response_200_type_1 import EmailVerificationResendResponse200Type1
from ...models.email_verification_resend_response_401 import EmailVerificationResendResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/email/resend",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = EmailVerificationResendResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = EmailVerificationResendResponse200Type1.from_dict(data)



            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = EmailVerificationResendResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401]:
    """ Resend the verification email

     Sends a new verification link to the authenticated account's current
    email address. If the address is already verified the call is a no-op.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401]
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

) -> EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401 | None:
    """ Resend the verification email

     Sends a new verification link to the authenticated account's current
    email address. If the address is already verified the call is a no-op.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401]:
    """ Resend the verification email

     Sends a new verification link to the authenticated account's current
    email address. If the address is already verified the call is a no-op.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401]
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

) -> EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401 | None:
    """ Resend the verification email

     Sends a new verification link to the authenticated account's current
    email address. If the address is already verified the call is a no-op.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailVerificationResendResponse200Type0 | EmailVerificationResendResponse200Type1 | EmailVerificationResendResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
