from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_note_download_url_response_200 import DictationNoteDownloadUrlResponse200
from ...models.dictation_note_download_url_response_401 import DictationNoteDownloadUrlResponse401
from ...models.dictation_note_download_url_response_403 import DictationNoteDownloadUrlResponse403
from ...models.dictation_note_download_url_response_404 import DictationNoteDownloadUrlResponse404
from typing import cast



def _get_kwargs(
    attachment: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/note-attachments/{attachment}/download-url".format(attachment=quote(str(attachment), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationNoteDownloadUrlResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationNoteDownloadUrlResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationNoteDownloadUrlResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationNoteDownloadUrlResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attachment: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404]:
    """ Get a download URL for a note attachment

     Returns a short-lived download URL for a single file attachment
    belonging to a note. The response contains the `url` that the caller
    should follow to fetch the file. Callers must have note access on
    the parent dictation.

    Args:
        attachment (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404]
     """


    kwargs = _get_kwargs(
        attachment=attachment,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    attachment: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404 | None:
    """ Get a download URL for a note attachment

     Returns a short-lived download URL for a single file attachment
    belonging to a note. The response contains the `url` that the caller
    should follow to fetch the file. Callers must have note access on
    the parent dictation.

    Args:
        attachment (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404
     """


    return sync_detailed(
        attachment=attachment,
client=client,

    ).parsed

async def asyncio_detailed(
    attachment: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404]:
    """ Get a download URL for a note attachment

     Returns a short-lived download URL for a single file attachment
    belonging to a note. The response contains the `url` that the caller
    should follow to fetch the file. Callers must have note access on
    the parent dictation.

    Args:
        attachment (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404]
     """


    kwargs = _get_kwargs(
        attachment=attachment,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    attachment: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404 | None:
    """ Get a download URL for a note attachment

     Returns a short-lived download URL for a single file attachment
    belonging to a note. The response contains the `url` that the caller
    should follow to fetch the file. Callers must have note access on
    the parent dictation.

    Args:
        attachment (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteDownloadUrlResponse200 | DictationNoteDownloadUrlResponse401 | DictationNoteDownloadUrlResponse403 | DictationNoteDownloadUrlResponse404
     """


    return (await asyncio_detailed(
        attachment=attachment,
client=client,

    )).parsed
