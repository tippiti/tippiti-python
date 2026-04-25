from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_note_update_body import DictationNoteUpdateBody
from ...models.dictation_note_update_response_200 import DictationNoteUpdateResponse200
from ...models.dictation_note_update_response_401 import DictationNoteUpdateResponse401
from ...models.dictation_note_update_response_403 import DictationNoteUpdateResponse403
from ...models.dictation_note_update_response_404 import DictationNoteUpdateResponse404
from ...models.dictation_note_update_response_422 import DictationNoteUpdateResponse422
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    note: str,
    *,
    body: DictationNoteUpdateBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/notes/{note}".format(note=quote(str(note), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationNoteUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationNoteUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationNoteUpdateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationNoteUpdateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationNoteUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422]:
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
    body: DictationNoteUpdateBody | Unset = UNSET,

) -> Response[DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422]:
    """ Update a note

     Updates a note's text content and the `is_important` / `show_on_top`
    flags. Pinning a note to the top implies importance; clearing the
    important flag also unpins the note. Only supplied fields are
    changed.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationNoteUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422]
     """


    kwargs = _get_kwargs(
        note=note,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    note: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationNoteUpdateBody | Unset = UNSET,

) -> DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422 | None:
    """ Update a note

     Updates a note's text content and the `is_important` / `show_on_top`
    flags. Pinning a note to the top implies importance; clearing the
    important flag also unpins the note. Only supplied fields are
    changed.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationNoteUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422
     """


    return sync_detailed(
        note=note,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    note: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationNoteUpdateBody | Unset = UNSET,

) -> Response[DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422]:
    """ Update a note

     Updates a note's text content and the `is_important` / `show_on_top`
    flags. Pinning a note to the top implies importance; clearing the
    important flag also unpins the note. Only supplied fields are
    changed.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationNoteUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422]
     """


    kwargs = _get_kwargs(
        note=note,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    note: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationNoteUpdateBody | Unset = UNSET,

) -> DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422 | None:
    """ Update a note

     Updates a note's text content and the `is_important` / `show_on_top`
    flags. Pinning a note to the top implies importance; clearing the
    important flag also unpins the note. Only supplied fields are
    changed.

    Args:
        note (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationNoteUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteUpdateResponse200 | DictationNoteUpdateResponse401 | DictationNoteUpdateResponse403 | DictationNoteUpdateResponse404 | DictationNoteUpdateResponse422
     """


    return (await asyncio_detailed(
        note=note,
client=client,
body=body,

    )).parsed
