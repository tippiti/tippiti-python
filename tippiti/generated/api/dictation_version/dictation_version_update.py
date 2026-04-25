from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_version_update_response_200 import DictationVersionUpdateResponse200
from ...models.dictation_version_update_response_401 import DictationVersionUpdateResponse401
from ...models.dictation_version_update_response_403 import DictationVersionUpdateResponse403
from ...models.dictation_version_update_response_404 import DictationVersionUpdateResponse404
from ...models.dictation_version_update_response_409 import DictationVersionUpdateResponse409
from ...models.dictation_version_update_response_422 import DictationVersionUpdateResponse422
from ...models.save_version_request import SaveVersionRequest
from typing import cast



def _get_kwargs(
    dictation: str,
    version: str,
    *,
    body: SaveVersionRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/dictations/{dictation}/versions/{version}".format(dictation=quote(str(dictation), safe=""),version=quote(str(version), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationVersionUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationVersionUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationVersionUpdateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationVersionUpdateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = DictationVersionUpdateResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = DictationVersionUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422]:
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
    body: SaveVersionRequest,

) -> Response[DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422]:
    """ Update a version's text in place

     Overwrites the text of an existing active version. Pending versions
    cannot be overwritten and the parent dictation must be completed.
    Callers may pass `expected_updated_at` for optimistic concurrency –
    a mismatch returns `409`. An identical text payload is a no-op.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        version (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (SaveVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
version=version,
body=body,

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
    body: SaveVersionRequest,

) -> DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422 | None:
    """ Update a version's text in place

     Overwrites the text of an existing active version. Pending versions
    cannot be overwritten and the parent dictation must be completed.
    Callers may pass `expected_updated_at` for optimistic concurrency –
    a mismatch returns `409`. An identical text payload is a no-op.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        version (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (SaveVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422
     """


    return sync_detailed(
        dictation=dictation,
version=version,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    version: str,
    *,
    client: AuthenticatedClient | Client,
    body: SaveVersionRequest,

) -> Response[DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422]:
    """ Update a version's text in place

     Overwrites the text of an existing active version. Pending versions
    cannot be overwritten and the parent dictation must be completed.
    Callers may pass `expected_updated_at` for optimistic concurrency –
    a mismatch returns `409`. An identical text payload is a no-op.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        version (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (SaveVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
version=version,
body=body,

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
    body: SaveVersionRequest,

) -> DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422 | None:
    """ Update a version's text in place

     Overwrites the text of an existing active version. Pending versions
    cannot be overwritten and the parent dictation must be completed.
    Callers may pass `expected_updated_at` for optimistic concurrency –
    a mismatch returns `409`. An identical text payload is a no-op.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        version (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (SaveVersionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationVersionUpdateResponse200 | DictationVersionUpdateResponse401 | DictationVersionUpdateResponse403 | DictationVersionUpdateResponse404 | DictationVersionUpdateResponse409 | DictationVersionUpdateResponse422
     """


    return (await asyncio_detailed(
        dictation=dictation,
version=version,
client=client,
body=body,

    )).parsed
