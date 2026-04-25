from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_version_reject_response_200 import DictationVersionRejectResponse200
from ...models.dictation_version_reject_response_401 import DictationVersionRejectResponse401
from ...models.dictation_version_reject_response_403 import DictationVersionRejectResponse403
from ...models.dictation_version_reject_response_404 import DictationVersionRejectResponse404
from ...models.dictation_version_reject_response_422 import DictationVersionRejectResponse422
from typing import cast



def _get_kwargs(
    dictation: str,
    version: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/{dictation}/versions/{version}/reject".format(dictation=quote(str(dictation), safe=""),version=quote(str(version), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationVersionRejectResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationVersionRejectResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationVersionRejectResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationVersionRejectResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationVersionRejectResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dictation: str,
    version: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422]:
    """ Reject a pending version

     Marks a pending version as rejected. The version number is preserved
    for continuity but the version is no longer offered as selectable.
    Fails with `422` if the version is not pending.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        version (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
version=version,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dictation: str,
    version: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422 | None:
    """ Reject a pending version

     Marks a pending version as rejected. The version number is preserved
    for continuity but the version is no longer offered as selectable.
    Fails with `422` if the version is not pending.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        version (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422
     """


    return sync_detailed(
        dictation=dictation,
version=version,
client=client,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    version: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422]:
    """ Reject a pending version

     Marks a pending version as rejected. The version number is preserved
    for continuity but the version is no longer offered as selectable.
    Fails with `422` if the version is not pending.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        version (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
version=version,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dictation: str,
    version: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422 | None:
    """ Reject a pending version

     Marks a pending version as rejected. The version number is preserved
    for continuity but the version is no longer offered as selectable.
    Fails with `422` if the version is not pending.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        version (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationVersionRejectResponse200 | DictationVersionRejectResponse401 | DictationVersionRejectResponse403 | DictationVersionRejectResponse404 | DictationVersionRejectResponse422
     """


    return (await asyncio_detailed(
        dictation=dictation,
version=version,
client=client,

    )).parsed
