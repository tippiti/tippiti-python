from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_show_response_200 import DictationShowResponse200
from ...models.dictation_show_response_401 import DictationShowResponse401
from ...models.dictation_show_response_403 import DictationShowResponse403
from ...models.dictation_show_response_404 import DictationShowResponse404
from typing import cast



def _get_kwargs(
    dictation: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dictations/{dictation}".format(dictation=quote(str(dictation), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationShowResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationShowResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationShowResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationShowResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404]:
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

) -> Response[DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404]:
    """ Get a single dictation

     Returns one dictation together with its folders, version history and
    processing log entries. Additional collections (shares, notes counts,
    attached sub-users) are included based on the caller's capabilities
    and whether they are a main user or a sub-user with access to the
    dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404]
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

) -> DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404 | None:
    """ Get a single dictation

     Returns one dictation together with its folders, version history and
    processing log entries. Additional collections (shares, notes counts,
    attached sub-users) are included based on the caller's capabilities
    and whether they are a main user or a sub-user with access to the
    dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404
     """


    return sync_detailed(
        dictation=dictation,
client=client,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404]:
    """ Get a single dictation

     Returns one dictation together with its folders, version history and
    processing log entries. Additional collections (shares, notes counts,
    attached sub-users) are included based on the caller's capabilities
    and whether they are a main user or a sub-user with access to the
    dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404]
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

) -> DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404 | None:
    """ Get a single dictation

     Returns one dictation together with its folders, version history and
    processing log entries. Additional collections (shares, notes counts,
    attached sub-users) are included based on the caller's capabilities
    and whether they are a main user or a sub-user with access to the
    dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShowResponse200 | DictationShowResponse401 | DictationShowResponse403 | DictationShowResponse404
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,

    )).parsed
