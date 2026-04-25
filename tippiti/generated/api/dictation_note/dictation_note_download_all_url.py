from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_note_download_all_url_response_200 import DictationNoteDownloadAllUrlResponse200
from ...models.dictation_note_download_all_url_response_401 import DictationNoteDownloadAllUrlResponse401
from ...models.dictation_note_download_all_url_response_403 import DictationNoteDownloadAllUrlResponse403
from ...models.dictation_note_download_all_url_response_404 import DictationNoteDownloadAllUrlResponse404
from typing import cast



def _get_kwargs(
    note: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/notes/{note}/attachments/download-all-url".format(note=quote(str(note), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationNoteDownloadAllUrlResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationNoteDownloadAllUrlResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationNoteDownloadAllUrlResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationNoteDownloadAllUrlResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    note: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404]:
    """ Get a download URL for all attachments of a note

     Returns a short-lived download URL that serves a ZIP archive of all
    file attachments on the given note. Fails with `404` when the note
    has no attachments. Callers must have note access on the parent
    dictation.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404]
     """


    kwargs = _get_kwargs(
        note=note,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    note: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404 | None:
    """ Get a download URL for all attachments of a note

     Returns a short-lived download URL that serves a ZIP archive of all
    file attachments on the given note. Fails with `404` when the note
    has no attachments. Callers must have note access on the parent
    dictation.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404
     """


    return sync_detailed(
        note=note,
client=client,

    ).parsed

async def asyncio_detailed(
    note: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404]:
    """ Get a download URL for all attachments of a note

     Returns a short-lived download URL that serves a ZIP archive of all
    file attachments on the given note. Fails with `404` when the note
    has no attachments. Callers must have note access on the parent
    dictation.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404]
     """


    kwargs = _get_kwargs(
        note=note,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    note: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404 | None:
    """ Get a download URL for all attachments of a note

     Returns a short-lived download URL that serves a ZIP archive of all
    file attachments on the given note. Fails with `404` when the note
    has no attachments. Callers must have note access on the parent
    dictation.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteDownloadAllUrlResponse200 | DictationNoteDownloadAllUrlResponse401 | DictationNoteDownloadAllUrlResponse403 | DictationNoteDownloadAllUrlResponse404
     """


    return (await asyncio_detailed(
        note=note,
client=client,

    )).parsed
