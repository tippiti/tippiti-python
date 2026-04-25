from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.instruction_set_instruction_presets_response_200 import InstructionSetInstructionPresetsResponse200
from ...models.instruction_set_instruction_presets_response_401 import InstructionSetInstructionPresetsResponse401
from ...models.instruction_set_instruction_presets_response_403 import InstructionSetInstructionPresetsResponse403
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/instruction-sets/presets/instructions",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403 | None:
    if response.status_code == 200:
        response_200 = InstructionSetInstructionPresetsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = InstructionSetInstructionPresetsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InstructionSetInstructionPresetsResponse403.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403]:
    """ List instruction presets

     Returns the catalogue of ready-made instruction presets that can be
    added to an instruction set. Each entry carries a `category` field
    for client-side grouping.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403 | None:
    """ List instruction presets

     Returns the catalogue of ready-made instruction presets that can be
    added to an instruction set. Each entry carries a `category` field
    for client-side grouping.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403]:
    """ List instruction presets

     Returns the catalogue of ready-made instruction presets that can be
    added to an instruction set. Each entry carries a `category` field
    for client-side grouping.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403 | None:
    """ List instruction presets

     Returns the catalogue of ready-made instruction presets that can be
    added to an instruction set. Each entry carries a `category` field
    for client-side grouping.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetInstructionPresetsResponse200 | InstructionSetInstructionPresetsResponse401 | InstructionSetInstructionPresetsResponse403
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
