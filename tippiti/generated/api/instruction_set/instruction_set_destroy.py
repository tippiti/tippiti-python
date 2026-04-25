from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.instruction_set_destroy_response_204 import InstructionSetDestroyResponse204
from ...models.instruction_set_destroy_response_401 import InstructionSetDestroyResponse401
from ...models.instruction_set_destroy_response_403 import InstructionSetDestroyResponse403
from ...models.instruction_set_destroy_response_404 import InstructionSetDestroyResponse404
from typing import cast



def _get_kwargs(
    instruction_set: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/instruction-sets/{instruction_set}".format(instruction_set=quote(str(instruction_set), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404 | None:
    if response.status_code == 204:
        response_204 = InstructionSetDestroyResponse204.from_dict(response.json())



        return response_204

    if response.status_code == 401:
        response_401 = InstructionSetDestroyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InstructionSetDestroyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = InstructionSetDestroyResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    instruction_set: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404]:
    """ Delete an instruction set

     Deletes an instruction set belonging to the authenticated account
    together with its instructions.

    Args:
        instruction_set (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404]
     """


    kwargs = _get_kwargs(
        instruction_set=instruction_set,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    instruction_set: str,
    *,
    client: AuthenticatedClient | Client,

) -> InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404 | None:
    """ Delete an instruction set

     Deletes an instruction set belonging to the authenticated account
    together with its instructions.

    Args:
        instruction_set (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404
     """


    return sync_detailed(
        instruction_set=instruction_set,
client=client,

    ).parsed

async def asyncio_detailed(
    instruction_set: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404]:
    """ Delete an instruction set

     Deletes an instruction set belonging to the authenticated account
    together with its instructions.

    Args:
        instruction_set (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404]
     """


    kwargs = _get_kwargs(
        instruction_set=instruction_set,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    instruction_set: str,
    *,
    client: AuthenticatedClient | Client,

) -> InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404 | None:
    """ Delete an instruction set

     Deletes an instruction set belonging to the authenticated account
    together with its instructions.

    Args:
        instruction_set (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetDestroyResponse204 | InstructionSetDestroyResponse401 | InstructionSetDestroyResponse403 | InstructionSetDestroyResponse404
     """


    return (await asyncio_detailed(
        instruction_set=instruction_set,
client=client,

    )).parsed
