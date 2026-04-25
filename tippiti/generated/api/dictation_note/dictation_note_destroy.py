from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_note_destroy_response_200 import DictationNoteDestroyResponse200
from ...models.dictation_note_destroy_response_401 import DictationNoteDestroyResponse401
from ...models.dictation_note_destroy_response_403 import DictationNoteDestroyResponse403
from ...models.dictation_note_destroy_response_404 import DictationNoteDestroyResponse404
from typing import cast



def _get_kwargs(
    note: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/notes/{note}".format(note=quote(str(note), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationNoteDestroyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationNoteDestroyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationNoteDestroyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationNoteDestroyResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404]:
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

) -> Response[DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404]:
    """ Delete a note

     Removes the note together with all of its file attachments. Only the
    note's author or a main user with access to the dictation may delete
    a note.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404]
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

) -> DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404 | None:
    """ Delete a note

     Removes the note together with all of its file attachments. Only the
    note's author or a main user with access to the dictation may delete
    a note.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404
     """


    return sync_detailed(
        note=note,
client=client,

    ).parsed

async def asyncio_detailed(
    note: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404]:
    """ Delete a note

     Removes the note together with all of its file attachments. Only the
    note's author or a main user with access to the dictation may delete
    a note.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404]
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

) -> DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404 | None:
    """ Delete a note

     Removes the note together with all of its file attachments. Only the
    note's author or a main user with access to the dictation may delete
    a note.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteDestroyResponse200 | DictationNoteDestroyResponse401 | DictationNoteDestroyResponse403 | DictationNoteDestroyResponse404
     """


    return (await asyncio_detailed(
        note=note,
client=client,

    )).parsed
