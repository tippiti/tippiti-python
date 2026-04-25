from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.notification_setting_update_body import NotificationSettingUpdateBody
from ...models.notification_setting_update_response_200 import NotificationSettingUpdateResponse200
from ...models.notification_setting_update_response_401 import NotificationSettingUpdateResponse401
from ...models.notification_setting_update_response_422 import NotificationSettingUpdateResponse422
from typing import cast



def _get_kwargs(
    *,
    body: NotificationSettingUpdateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/account/notifications",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = NotificationSettingUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = NotificationSettingUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = NotificationSettingUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NotificationSettingUpdateBody,

) -> Response[NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422]:
    """ Update notification preferences

     Updates the authenticated account's notification preferences. The
    request body carries a `settings` map keyed by preference – each entry
    may toggle the notification, choose whether the account itself receives
    it, list additional recipient email addresses, set per-field visibility
    and configure custom template options. Some templates cannot be turned
    off; enabled templates without any recipients fall back to delivering
    to the account itself.

    Args:
        body (NotificationSettingUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422]
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
    body: NotificationSettingUpdateBody,

) -> NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422 | None:
    """ Update notification preferences

     Updates the authenticated account's notification preferences. The
    request body carries a `settings` map keyed by preference – each entry
    may toggle the notification, choose whether the account itself receives
    it, list additional recipient email addresses, set per-field visibility
    and configure custom template options. Some templates cannot be turned
    off; enabled templates without any recipients fall back to delivering
    to the account itself.

    Args:
        body (NotificationSettingUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NotificationSettingUpdateBody,

) -> Response[NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422]:
    """ Update notification preferences

     Updates the authenticated account's notification preferences. The
    request body carries a `settings` map keyed by preference – each entry
    may toggle the notification, choose whether the account itself receives
    it, list additional recipient email addresses, set per-field visibility
    and configure custom template options. Some templates cannot be turned
    off; enabled templates without any recipients fall back to delivering
    to the account itself.

    Args:
        body (NotificationSettingUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422]
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
    body: NotificationSettingUpdateBody,

) -> NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422 | None:
    """ Update notification preferences

     Updates the authenticated account's notification preferences. The
    request body carries a `settings` map keyed by preference – each entry
    may toggle the notification, choose whether the account itself receives
    it, list additional recipient email addresses, set per-field visibility
    and configure custom template options. Some templates cannot be turned
    off; enabled templates without any recipients fall back to delivering
    to the account itself.

    Args:
        body (NotificationSettingUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationSettingUpdateResponse200 | NotificationSettingUpdateResponse401 | NotificationSettingUpdateResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
