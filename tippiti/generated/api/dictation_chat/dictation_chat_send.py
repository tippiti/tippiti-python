from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_chat_send_body import DictationChatSendBody
from ...models.dictation_chat_send_response_200 import DictationChatSendResponse200
from ...models.dictation_chat_send_response_401 import DictationChatSendResponse401
from ...models.dictation_chat_send_response_403_type_0 import DictationChatSendResponse403Type0
from ...models.dictation_chat_send_response_403_type_1 import DictationChatSendResponse403Type1
from ...models.dictation_chat_send_response_404 import DictationChatSendResponse404
from ...models.dictation_chat_send_response_422 import DictationChatSendResponse422
from typing import cast



def _get_kwargs(
    dictation: str,
    *,
    body: DictationChatSendBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/{dictation}/chat".format(dictation=quote(str(dictation), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationChatSendResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationChatSendResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        def _parse_response_403(data: object) -> DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = DictationChatSendResponse403Type0.from_dict(data)



                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_1 = DictationChatSendResponse403Type1.from_dict(data)



            return response_403_type_1

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DictationChatSendResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationChatSendResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationChatSendBody,

) -> Response[DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422]:
    """ Send a chat message to the dictation assistant

     Sends a user message for a completed dictation and streams the
    assistant's reply as Server-Sent Events. The assistant replies based
    on the dictation's content. Requires the dictation to be in a
    completed state and within its chat allowance; exceeded allowances
    return `403`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationChatSendBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationChatSendBody,

) -> DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422 | None:
    """ Send a chat message to the dictation assistant

     Sends a user message for a completed dictation and streams the
    assistant's reply as Server-Sent Events. The assistant replies based
    on the dictation's content. Requires the dictation to be in a
    completed state and within its chat allowance; exceeded allowances
    return `403`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationChatSendBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422
     """


    return sync_detailed(
        dictation=dictation,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationChatSendBody,

) -> Response[DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422]:
    """ Send a chat message to the dictation assistant

     Sends a user message for a completed dictation and streams the
    assistant's reply as Server-Sent Events. The assistant replies based
    on the dictation's content. Requires the dictation to be in a
    completed state and within its chat allowance; exceeded allowances
    return `403`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationChatSendBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationChatSendBody,

) -> DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422 | None:
    """ Send a chat message to the dictation assistant

     Sends a user message for a completed dictation and streams the
    assistant's reply as Server-Sent Events. The assistant replies based
    on the dictation's content. Requires the dictation to be in a
    completed state and within its chat allowance; exceeded allowances
    return `403`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationChatSendBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationChatSendResponse200 | DictationChatSendResponse401 | DictationChatSendResponse403Type0 | DictationChatSendResponse403Type1 | DictationChatSendResponse404 | DictationChatSendResponse422
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,
body=body,

    )).parsed
