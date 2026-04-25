from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_stream_audio_response_200 import DictationStreamAudioResponse200
from ...models.dictation_stream_audio_response_401 import DictationStreamAudioResponse401
from ...models.dictation_stream_audio_response_403 import DictationStreamAudioResponse403
from ...models.dictation_stream_audio_response_404 import DictationStreamAudioResponse404
from typing import cast



def _get_kwargs(
    dictation: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dictations/{dictation}/audio-stream".format(dictation=quote(str(dictation), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationStreamAudioResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationStreamAudioResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationStreamAudioResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationStreamAudioResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404]:
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

) -> Response[DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404]:
    """ Get a short-lived streaming URL for the dictation audio

     Returns a `url` suitable for direct playback by an audio player,
    together with the `token` embedded in it. The URL is short-lived and
    must be kept confidential. Returns `404` when no audio file is
    available.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404]
     """


    kwargs = _get_kwargs(
        dictation=dictation,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404 | None:
    """ Get a short-lived streaming URL for the dictation audio

     Returns a `url` suitable for direct playback by an audio player,
    together with the `token` embedded in it. The URL is short-lived and
    must be kept confidential. Returns `404` when no audio file is
    available.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404
     """


    return sync_detailed(
        dictation=dictation,
client=client,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404]:
    """ Get a short-lived streaming URL for the dictation audio

     Returns a `url` suitable for direct playback by an audio player,
    together with the `token` embedded in it. The URL is short-lived and
    must be kept confidential. Returns `404` when no audio file is
    available.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404]
     """


    kwargs = _get_kwargs(
        dictation=dictation,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404 | None:
    """ Get a short-lived streaming URL for the dictation audio

     Returns a `url` suitable for direct playback by an audio player,
    together with the `token` embedded in it. The URL is short-lived and
    must be kept confidential. Returns `404` when no audio file is
    available.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationStreamAudioResponse200 | DictationStreamAudioResponse401 | DictationStreamAudioResponse403 | DictationStreamAudioResponse404
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,

    )).parsed
