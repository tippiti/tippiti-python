from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_bulk_restore_body import DictationBulkRestoreBody
from ...models.dictation_bulk_restore_response_200 import DictationBulkRestoreResponse200
from ...models.dictation_bulk_restore_response_401 import DictationBulkRestoreResponse401
from ...models.dictation_bulk_restore_response_403 import DictationBulkRestoreResponse403
from ...models.dictation_bulk_restore_response_422 import DictationBulkRestoreResponse422
from typing import cast



def _get_kwargs(
    *,
    body: DictationBulkRestoreBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/bulk/restore",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationBulkRestoreResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationBulkRestoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationBulkRestoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = DictationBulkRestoreResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DictationBulkRestoreBody,

) -> Response[DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422]:
    """ Restore multiple archived dictations at once

     Accepts an `ids` array and unarchives each dictation the caller has
    access to. Requires the archive capability. Unknown or inaccessible
    IDs are ignored.

    Args:
        body (DictationBulkRestoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DictationBulkRestoreBody,

) -> DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422 | None:
    """ Restore multiple archived dictations at once

     Accepts an `ids` array and unarchives each dictation the caller has
    access to. Requires the archive capability. Unknown or inaccessible
    IDs are ignored.

    Args:
        body (DictationBulkRestoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DictationBulkRestoreBody,

) -> Response[DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422]:
    """ Restore multiple archived dictations at once

     Accepts an `ids` array and unarchives each dictation the caller has
    access to. Requires the archive capability. Unknown or inaccessible
    IDs are ignored.

    Args:
        body (DictationBulkRestoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DictationBulkRestoreBody,

) -> DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422 | None:
    """ Restore multiple archived dictations at once

     Accepts an `ids` array and unarchives each dictation the caller has
    access to. Requires the archive capability. Unknown or inaccessible
    IDs are ignored.

    Args:
        body (DictationBulkRestoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationBulkRestoreResponse200 | DictationBulkRestoreResponse401 | DictationBulkRestoreResponse403 | DictationBulkRestoreResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
