from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_destroy_response_204 import DictationDestroyResponse204
from ...models.dictation_destroy_response_401 import DictationDestroyResponse401
from ...models.dictation_destroy_response_403 import DictationDestroyResponse403
from ...models.dictation_destroy_response_404 import DictationDestroyResponse404
from ...models.dictation_destroy_response_409 import DictationDestroyResponse409
from typing import cast



def _get_kwargs(
    dictation: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/dictations/{dictation}".format(dictation=quote(str(dictation), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409 | None:
    if response.status_code == 204:
        response_204 = DictationDestroyResponse204.from_dict(response.json())



        return response_204

    if response.status_code == 401:
        response_401 = DictationDestroyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationDestroyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationDestroyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = DictationDestroyResponse409.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409]:
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

) -> Response[DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409]:
    """ Delete a dictation

     Permanently removes the dictation together with its transcript,
    attached audio and notes. Requires the delete capability – sub-users
    without it receive `403`. Dictations that are still being processed
    cannot be deleted and return `409`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409]
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

) -> DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409 | None:
    """ Delete a dictation

     Permanently removes the dictation together with its transcript,
    attached audio and notes. Requires the delete capability – sub-users
    without it receive `403`. Dictations that are still being processed
    cannot be deleted and return `409`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409
     """


    return sync_detailed(
        dictation=dictation,
client=client,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409]:
    """ Delete a dictation

     Permanently removes the dictation together with its transcript,
    attached audio and notes. Requires the delete capability – sub-users
    without it receive `403`. Dictations that are still being processed
    cannot be deleted and return `409`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409]
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

) -> DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409 | None:
    """ Delete a dictation

     Permanently removes the dictation together with its transcript,
    attached audio and notes. Requires the delete capability – sub-users
    without it receive `403`. Dictations that are still being processed
    cannot be deleted and return `409`.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationDestroyResponse204 | DictationDestroyResponse401 | DictationDestroyResponse403 | DictationDestroyResponse404 | DictationDestroyResponse409
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,

    )).parsed
