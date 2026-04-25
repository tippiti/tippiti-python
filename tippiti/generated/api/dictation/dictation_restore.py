from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_restore_response_200 import DictationRestoreResponse200
from ...models.dictation_restore_response_401 import DictationRestoreResponse401
from ...models.dictation_restore_response_403 import DictationRestoreResponse403
from ...models.dictation_restore_response_404 import DictationRestoreResponse404
from typing import cast



def _get_kwargs(
    dictation: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/{dictation}/restore".format(dictation=quote(str(dictation), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationRestoreResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationRestoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationRestoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationRestoreResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404]:
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

) -> Response[DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404]:
    """ Restore an archived dictation

     Reverts a previously archived dictation to the active state so it
    reappears in the default listing. Requires the archive capability.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404]
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

) -> DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404 | None:
    """ Restore an archived dictation

     Reverts a previously archived dictation to the active state so it
    reappears in the default listing. Requires the archive capability.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404
     """


    return sync_detailed(
        dictation=dictation,
client=client,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404]:
    """ Restore an archived dictation

     Reverts a previously archived dictation to the active state so it
    reappears in the default listing. Requires the archive capability.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404]
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

) -> DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404 | None:
    """ Restore an archived dictation

     Reverts a previously archived dictation to the active state so it
    reappears in the default listing. Requires the archive capability.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationRestoreResponse200 | DictationRestoreResponse401 | DictationRestoreResponse403 | DictationRestoreResponse404
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,

    )).parsed
