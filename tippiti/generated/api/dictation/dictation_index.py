from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_index_response_200 import DictationIndexResponse200
from ...models.dictation_index_response_401 import DictationIndexResponse401
from ...models.dictation_index_response_403 import DictationIndexResponse403
from ...models.dictation_index_response_422 import DictationIndexResponse422
from ...models.dictation_index_scope import DictationIndexScope
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    scope: DictationIndexScope | Unset = UNSET,
    include_notes: bool | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope.value

    params["scope"] = json_scope

    json_include_notes: bool | None | Unset
    if isinstance(include_notes, Unset):
        json_include_notes = UNSET
    else:
        json_include_notes = include_notes
    params["include_notes"] = json_include_notes


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dictations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = DictationIndexResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    scope: DictationIndexScope | Unset = UNSET,
    include_notes: bool | None | Unset = UNSET,

) -> Response[DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422]:
    """ List dictations visible to the authenticated account

     Returns dictations owned by a main user, or – for sub-users – the
    dictations their parent account has granted them access to (all, a
    specific set or folder-based). The `scope` query parameter toggles
    between active (default) and archived dictations. Set `include_notes=1`
    to load attached notes inline; this requires the note capability and
    mixes archived and active dictations.

    Args:
        scope (DictationIndexScope | Unset):
        include_notes (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422]
     """


    kwargs = _get_kwargs(
        scope=scope,
include_notes=include_notes,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    scope: DictationIndexScope | Unset = UNSET,
    include_notes: bool | None | Unset = UNSET,

) -> DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422 | None:
    """ List dictations visible to the authenticated account

     Returns dictations owned by a main user, or – for sub-users – the
    dictations their parent account has granted them access to (all, a
    specific set or folder-based). The `scope` query parameter toggles
    between active (default) and archived dictations. Set `include_notes=1`
    to load attached notes inline; this requires the note capability and
    mixes archived and active dictations.

    Args:
        scope (DictationIndexScope | Unset):
        include_notes (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422
     """


    return sync_detailed(
        client=client,
scope=scope,
include_notes=include_notes,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    scope: DictationIndexScope | Unset = UNSET,
    include_notes: bool | None | Unset = UNSET,

) -> Response[DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422]:
    """ List dictations visible to the authenticated account

     Returns dictations owned by a main user, or – for sub-users – the
    dictations their parent account has granted them access to (all, a
    specific set or folder-based). The `scope` query parameter toggles
    between active (default) and archived dictations. Set `include_notes=1`
    to load attached notes inline; this requires the note capability and
    mixes archived and active dictations.

    Args:
        scope (DictationIndexScope | Unset):
        include_notes (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422]
     """


    kwargs = _get_kwargs(
        scope=scope,
include_notes=include_notes,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    scope: DictationIndexScope | Unset = UNSET,
    include_notes: bool | None | Unset = UNSET,

) -> DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422 | None:
    """ List dictations visible to the authenticated account

     Returns dictations owned by a main user, or – for sub-users – the
    dictations their parent account has granted them access to (all, a
    specific set or folder-based). The `scope` query parameter toggles
    between active (default) and archived dictations. Set `include_notes=1`
    to load attached notes inline; this requires the note capability and
    mixes archived and active dictations.

    Args:
        scope (DictationIndexScope | Unset):
        include_notes (bool | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationIndexResponse200 | DictationIndexResponse401 | DictationIndexResponse403 | DictationIndexResponse422
     """


    return (await asyncio_detailed(
        client=client,
scope=scope,
include_notes=include_notes,

    )).parsed
