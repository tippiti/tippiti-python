from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_refresh_audio_stream_response_200 import DictationRefreshAudioStreamResponse200
from ...models.dictation_refresh_audio_stream_response_401 import DictationRefreshAudioStreamResponse401
from ...models.dictation_refresh_audio_stream_response_403 import DictationRefreshAudioStreamResponse403
from ...models.dictation_refresh_audio_stream_response_404 import DictationRefreshAudioStreamResponse404
from typing import cast



def _get_kwargs(
    token: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/audio-stream/{token}/refresh".format(token=quote(str(token), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationRefreshAudioStreamResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationRefreshAudioStreamResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationRefreshAudioStreamResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationRefreshAudioStreamResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404]:
    """ Keep an active audio streaming URL alive

     Extends the lifetime of an existing audio-stream token while playback
    is ongoing. The caller must still have permission to view the
    associated dictation; access revoked after the stream started causes
    subsequent refreshes to fail. Returns `404` for unknown or expired
    tokens.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    token: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404 | None:
    """ Keep an active audio streaming URL alive

     Extends the lifetime of an existing audio-stream token while playback
    is ongoing. The caller must still have permission to view the
    associated dictation; access revoked after the stream started causes
    subsequent refreshes to fail. Returns `404` for unknown or expired
    tokens.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404
     """


    return sync_detailed(
        token=token,
client=client,

    ).parsed

async def asyncio_detailed(
    token: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404]:
    """ Keep an active audio streaming URL alive

     Extends the lifetime of an existing audio-stream token while playback
    is ongoing. The caller must still have permission to view the
    associated dictation; access revoked after the stream started causes
    subsequent refreshes to fail. Returns `404` for unknown or expired
    tokens.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404]
     """


    kwargs = _get_kwargs(
        token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    token: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404 | None:
    """ Keep an active audio streaming URL alive

     Extends the lifetime of an existing audio-stream token while playback
    is ongoing. The caller must still have permission to view the
    associated dictation; access revoked after the stream started causes
    subsequent refreshes to fail. Returns `404` for unknown or expired
    tokens.

    Args:
        token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationRefreshAudioStreamResponse200 | DictationRefreshAudioStreamResponse401 | DictationRefreshAudioStreamResponse403 | DictationRefreshAudioStreamResponse404
     """


    return (await asyncio_detailed(
        token=token,
client=client,

    )).parsed
