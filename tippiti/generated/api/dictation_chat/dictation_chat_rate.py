from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_chat_rate_body import DictationChatRateBody
from ...models.dictation_chat_rate_response_200 import DictationChatRateResponse200
from ...models.dictation_chat_rate_response_401 import DictationChatRateResponse401
from ...models.dictation_chat_rate_response_403 import DictationChatRateResponse403
from ...models.dictation_chat_rate_response_404 import DictationChatRateResponse404
from ...models.dictation_chat_rate_response_422 import DictationChatRateResponse422
from typing import cast



def _get_kwargs(
    dictation: str,
    chat: str,
    *,
    body: DictationChatRateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/{dictation}/chat/{chat}/rate".format(dictation=quote(str(dictation), safe=""),chat=quote(str(chat), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationChatRateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationChatRateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationChatRateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationChatRateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationChatRateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dictation: str,
    chat: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationChatRateBody,

) -> Response[DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422]:
    """ Rate an assistant chat message

     Records a thumbs-up or thumbs-down rating for a single assistant
    reply. Only messages with role `assistant` belonging to the given
    dictation may be rated; user and system messages are rejected.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        chat (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationChatRateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
chat=chat,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dictation: str,
    chat: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationChatRateBody,

) -> DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422 | None:
    """ Rate an assistant chat message

     Records a thumbs-up or thumbs-down rating for a single assistant
    reply. Only messages with role `assistant` belonging to the given
    dictation may be rated; user and system messages are rejected.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        chat (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationChatRateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422
     """


    return sync_detailed(
        dictation=dictation,
chat=chat,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    chat: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationChatRateBody,

) -> Response[DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422]:
    """ Rate an assistant chat message

     Records a thumbs-up or thumbs-down rating for a single assistant
    reply. Only messages with role `assistant` belonging to the given
    dictation may be rated; user and system messages are rejected.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        chat (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationChatRateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
chat=chat,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dictation: str,
    chat: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationChatRateBody,

) -> DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422 | None:
    """ Rate an assistant chat message

     Records a thumbs-up or thumbs-down rating for a single assistant
    reply. Only messages with role `assistant` belonging to the given
    dictation may be rated; user and system messages are rejected.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        chat (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationChatRateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationChatRateResponse200 | DictationChatRateResponse401 | DictationChatRateResponse403 | DictationChatRateResponse404 | DictationChatRateResponse422
     """


    return (await asyncio_detailed(
        dictation=dictation,
chat=chat,
client=client,
body=body,

    )).parsed
