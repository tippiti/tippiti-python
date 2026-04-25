from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_store_body import DictationStoreBody
from ...models.dictation_store_response_201 import DictationStoreResponse201
from ...models.dictation_store_response_401 import DictationStoreResponse401
from ...models.dictation_store_response_402 import DictationStoreResponse402
from ...models.dictation_store_response_403 import DictationStoreResponse403
from ...models.dictation_store_response_422 import DictationStoreResponse422
from typing import cast



def _get_kwargs(
    *,
    body: DictationStoreBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations",
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422 | None:
    if response.status_code == 201:
        response_201 = DictationStoreResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = DictationStoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = DictationStoreResponse402.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = DictationStoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = DictationStoreResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DictationStoreBody,

) -> Response[DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422]:
    """ Upload a new dictation

     Accepts a multipart upload containing an audio or video `file` together
    with a required `title` and optional `client_name` and `comment`.
    Processing begins after upload and the response returns the created
    dictation in its initial pending state. Optional fields
    `instruction_set_id`, `folders` and `shared_with` are honoured only
    when the caller has the matching capability; main users may additionally
    share the new dictation with selected sub-users. Uploads are rejected
    with `402` when the account's character balance is depleted.

    Args:
        body (DictationStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422]
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
    body: DictationStoreBody,

) -> DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422 | None:
    """ Upload a new dictation

     Accepts a multipart upload containing an audio or video `file` together
    with a required `title` and optional `client_name` and `comment`.
    Processing begins after upload and the response returns the created
    dictation in its initial pending state. Optional fields
    `instruction_set_id`, `folders` and `shared_with` are honoured only
    when the caller has the matching capability; main users may additionally
    share the new dictation with selected sub-users. Uploads are rejected
    with `402` when the account's character balance is depleted.

    Args:
        body (DictationStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DictationStoreBody,

) -> Response[DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422]:
    """ Upload a new dictation

     Accepts a multipart upload containing an audio or video `file` together
    with a required `title` and optional `client_name` and `comment`.
    Processing begins after upload and the response returns the created
    dictation in its initial pending state. Optional fields
    `instruction_set_id`, `folders` and `shared_with` are honoured only
    when the caller has the matching capability; main users may additionally
    share the new dictation with selected sub-users. Uploads are rejected
    with `402` when the account's character balance is depleted.

    Args:
        body (DictationStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422]
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
    body: DictationStoreBody,

) -> DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422 | None:
    """ Upload a new dictation

     Accepts a multipart upload containing an audio or video `file` together
    with a required `title` and optional `client_name` and `comment`.
    Processing begins after upload and the response returns the created
    dictation in its initial pending state. Optional fields
    `instruction_set_id`, `folders` and `shared_with` are honoured only
    when the caller has the matching capability; main users may additionally
    share the new dictation with selected sub-users. Uploads are rejected
    with `402` when the account's character balance is depleted.

    Args:
        body (DictationStoreBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationStoreResponse201 | DictationStoreResponse401 | DictationStoreResponse402 | DictationStoreResponse403 | DictationStoreResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
