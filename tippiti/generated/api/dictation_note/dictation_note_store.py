from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_note_store_response_201 import DictationNoteStoreResponse201
from ...models.dictation_note_store_response_401 import DictationNoteStoreResponse401
from ...models.dictation_note_store_response_403 import DictationNoteStoreResponse403
from ...models.dictation_note_store_response_404 import DictationNoteStoreResponse404
from ...models.dictation_note_store_response_422 import DictationNoteStoreResponse422
from ...models.store_dictation_note_request import StoreDictationNoteRequest
from typing import cast



def _get_kwargs(
    dictation: str,
    *,
    body: StoreDictationNoteRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/{dictation}/notes".format(dictation=quote(str(dictation), safe=""),),
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422 | None:
    if response.status_code == 201:
        response_201 = DictationNoteStoreResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = DictationNoteStoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationNoteStoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationNoteStoreResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationNoteStoreResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422]:
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
    body: StoreDictationNoteRequest,

) -> Response[DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422]:
    """ Create a note on a dictation

     Creates a note with optional text content and file attachments on the
    given dictation. The `is_important` and `show_on_top` flags control
    visibility – a pinned note is always marked important. Other users
    with access to the dictation are notified by email.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (StoreDictationNoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422]
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
    body: StoreDictationNoteRequest,

) -> DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422 | None:
    """ Create a note on a dictation

     Creates a note with optional text content and file attachments on the
    given dictation. The `is_important` and `show_on_top` flags control
    visibility – a pinned note is always marked important. Other users
    with access to the dictation are notified by email.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (StoreDictationNoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422
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
    body: StoreDictationNoteRequest,

) -> Response[DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422]:
    """ Create a note on a dictation

     Creates a note with optional text content and file attachments on the
    given dictation. The `is_important` and `show_on_top` flags control
    visibility – a pinned note is always marked important. Other users
    with access to the dictation are notified by email.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (StoreDictationNoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422]
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
    body: StoreDictationNoteRequest,

) -> DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422 | None:
    """ Create a note on a dictation

     Creates a note with optional text content and file attachments on the
    given dictation. The `is_important` and `show_on_top` flags control
    visibility – a pinned note is always marked important. Other users
    with access to the dictation are notified by email.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (StoreDictationNoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationNoteStoreResponse201 | DictationNoteStoreResponse401 | DictationNoteStoreResponse403 | DictationNoteStoreResponse404 | DictationNoteStoreResponse422
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,
body=body,

    )).parsed
