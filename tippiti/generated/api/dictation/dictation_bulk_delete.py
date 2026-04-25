from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_bulk_delete_body import DictationBulkDeleteBody
from ...models.dictation_bulk_delete_response_200 import DictationBulkDeleteResponse200
from ...models.dictation_bulk_delete_response_401 import DictationBulkDeleteResponse401
from ...models.dictation_bulk_delete_response_403 import DictationBulkDeleteResponse403
from ...models.dictation_bulk_delete_response_422 import DictationBulkDeleteResponse422
from typing import cast



def _get_kwargs(
    *,
    body: DictationBulkDeleteBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/bulk/delete",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationBulkDeleteResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationBulkDeleteResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationBulkDeleteResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = DictationBulkDeleteResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DictationBulkDeleteBody,

) -> Response[DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422]:
    """ Delete multiple dictations at once

     Accepts an `ids` array and permanently removes every accessible
    dictation in it that is not currently being processed. Requires the
    delete capability. Returns `422` when none of the supplied IDs could
    be deleted.

    Args:
        body (DictationBulkDeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422]
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
    body: DictationBulkDeleteBody,

) -> DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422 | None:
    """ Delete multiple dictations at once

     Accepts an `ids` array and permanently removes every accessible
    dictation in it that is not currently being processed. Requires the
    delete capability. Returns `422` when none of the supplied IDs could
    be deleted.

    Args:
        body (DictationBulkDeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DictationBulkDeleteBody,

) -> Response[DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422]:
    """ Delete multiple dictations at once

     Accepts an `ids` array and permanently removes every accessible
    dictation in it that is not currently being processed. Requires the
    delete capability. Returns `422` when none of the supplied IDs could
    be deleted.

    Args:
        body (DictationBulkDeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422]
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
    body: DictationBulkDeleteBody,

) -> DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422 | None:
    """ Delete multiple dictations at once

     Accepts an `ids` array and permanently removes every accessible
    dictation in it that is not currently being processed. Requires the
    delete capability. Returns `422` when none of the supplied IDs could
    be deleted.

    Args:
        body (DictationBulkDeleteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationBulkDeleteResponse200 | DictationBulkDeleteResponse401 | DictationBulkDeleteResponse403 | DictationBulkDeleteResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
