from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.instruction_set_store_response_201 import InstructionSetStoreResponse201
from ...models.instruction_set_store_response_401 import InstructionSetStoreResponse401
from ...models.instruction_set_store_response_403 import InstructionSetStoreResponse403
from ...models.instruction_set_store_response_422 import InstructionSetStoreResponse422
from ...models.store_instruction_set_request import StoreInstructionSetRequest
from typing import cast



def _get_kwargs(
    *,
    body: StoreInstructionSetRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/instruction-sets",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422 | None:
    if response.status_code == 201:
        response_201 = InstructionSetStoreResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = InstructionSetStoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InstructionSetStoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = InstructionSetStoreResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StoreInstructionSetRequest,

) -> Response[InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422]:
    """ Create an instruction set

     Creates a new dictation instruction set with an optional list of
    instructions and text replacements. The set is owned by the
    authenticated account and returned with its nested instructions and
    replacements.

    Args:
        body (StoreInstructionSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422]
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
    body: StoreInstructionSetRequest,

) -> InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422 | None:
    """ Create an instruction set

     Creates a new dictation instruction set with an optional list of
    instructions and text replacements. The set is owned by the
    authenticated account and returned with its nested instructions and
    replacements.

    Args:
        body (StoreInstructionSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StoreInstructionSetRequest,

) -> Response[InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422]:
    """ Create an instruction set

     Creates a new dictation instruction set with an optional list of
    instructions and text replacements. The set is owned by the
    authenticated account and returned with its nested instructions and
    replacements.

    Args:
        body (StoreInstructionSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422]
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
    body: StoreInstructionSetRequest,

) -> InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422 | None:
    """ Create an instruction set

     Creates a new dictation instruction set with an optional list of
    instructions and text replacements. The set is owned by the
    authenticated account and returned with its nested instructions and
    replacements.

    Args:
        body (StoreInstructionSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetStoreResponse201 | InstructionSetStoreResponse401 | InstructionSetStoreResponse403 | InstructionSetStoreResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
