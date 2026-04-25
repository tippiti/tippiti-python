from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_version_index_response_200 import DictationVersionIndexResponse200
from ...models.dictation_version_index_response_401 import DictationVersionIndexResponse401
from ...models.dictation_version_index_response_403 import DictationVersionIndexResponse403
from ...models.dictation_version_index_response_404 import DictationVersionIndexResponse404
from typing import cast



def _get_kwargs(
    dictation: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dictations/{dictation}/versions".format(dictation=quote(str(dictation), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationVersionIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationVersionIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationVersionIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationVersionIndexResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404]:
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

) -> Response[DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404]:
    """ List versions of a dictation

     Returns metadata for all non-rejected versions of the given dictation
    – version number, status, source and last-modified timestamp. The
    text body is omitted to keep the response lightweight. Available to
    any caller who can view the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404]
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

) -> DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404 | None:
    """ List versions of a dictation

     Returns metadata for all non-rejected versions of the given dictation
    – version number, status, source and last-modified timestamp. The
    text body is omitted to keep the response lightweight. Available to
    any caller who can view the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404
     """


    return sync_detailed(
        dictation=dictation,
client=client,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404]:
    """ List versions of a dictation

     Returns metadata for all non-rejected versions of the given dictation
    – version number, status, source and last-modified timestamp. The
    text body is omitted to keep the response lightweight. Available to
    any caller who can view the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404]
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

) -> DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404 | None:
    """ List versions of a dictation

     Returns metadata for all non-rejected versions of the given dictation
    – version number, status, source and last-modified timestamp. The
    text body is omitted to keep the response lightweight. Available to
    any caller who can view the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationVersionIndexResponse200 | DictationVersionIndexResponse401 | DictationVersionIndexResponse403 | DictationVersionIndexResponse404
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,

    )).parsed
