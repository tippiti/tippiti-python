from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_share_send_email_body import DictationShareSendEmailBody
from ...models.dictation_share_send_email_response_200 import DictationShareSendEmailResponse200
from ...models.dictation_share_send_email_response_401 import DictationShareSendEmailResponse401
from ...models.dictation_share_send_email_response_403 import DictationShareSendEmailResponse403
from ...models.dictation_share_send_email_response_404 import DictationShareSendEmailResponse404
from ...models.dictation_share_send_email_response_422 import DictationShareSendEmailResponse422
from typing import cast



def _get_kwargs(
    share: str,
    *,
    body: DictationShareSendEmailBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/shares/{share}/send".format(share=quote(str(share), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationShareSendEmailResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationShareSendEmailResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationShareSendEmailResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationShareSendEmailResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationShareSendEmailResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareSendEmailBody,

) -> Response[DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422]:
    """ Send a share link by email

     Emails the share link to up to five recipient addresses with an
    optional personal `message`. If the share is password-protected, the
    password is only included in the email when `include_password` is
    true and the supplied `password` matches the share's password.
    Expired shares are rejected with `422`.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareSendEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422]
     """


    kwargs = _get_kwargs(
        share=share,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareSendEmailBody,

) -> DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422 | None:
    """ Send a share link by email

     Emails the share link to up to five recipient addresses with an
    optional personal `message`. If the share is password-protected, the
    password is only included in the email when `include_password` is
    true and the supplied `password` matches the share's password.
    Expired shares are rejected with `422`.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareSendEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422
     """


    return sync_detailed(
        share=share,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareSendEmailBody,

) -> Response[DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422]:
    """ Send a share link by email

     Emails the share link to up to five recipient addresses with an
    optional personal `message`. If the share is password-protected, the
    password is only included in the email when `include_password` is
    true and the supplied `password` matches the share's password.
    Expired shares are rejected with `422`.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareSendEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422]
     """


    kwargs = _get_kwargs(
        share=share,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    share: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationShareSendEmailBody,

) -> DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422 | None:
    """ Send a share link by email

     Emails the share link to up to five recipient addresses with an
    optional personal `message`. If the share is password-protected, the
    password is only included in the email when `include_password` is
    true and the supplied `password` matches the share's password.
    Expired shares are rejected with `422`.

    Args:
        share (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationShareSendEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareSendEmailResponse200 | DictationShareSendEmailResponse401 | DictationShareSendEmailResponse403 | DictationShareSendEmailResponse404 | DictationShareSendEmailResponse422
     """


    return (await asyncio_detailed(
        share=share,
client=client,
body=body,

    )).parsed
