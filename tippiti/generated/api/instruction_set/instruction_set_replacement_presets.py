from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.instruction_set_replacement_presets_response_200 import InstructionSetReplacementPresetsResponse200
from ...models.instruction_set_replacement_presets_response_401 import InstructionSetReplacementPresetsResponse401
from ...models.instruction_set_replacement_presets_response_403 import InstructionSetReplacementPresetsResponse403
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/instruction-sets/presets/replacements",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403 | None:
    if response.status_code == 200:
        response_200 = InstructionSetReplacementPresetsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = InstructionSetReplacementPresetsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InstructionSetReplacementPresetsResponse403.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403]:
    """ List replacement presets

     Returns the catalogue of optional text-replacement presets that can be
    added to an instruction set, including a suggested default-active flag
    per entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403]
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

) -> InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403 | None:
    """ List replacement presets

     Returns the catalogue of optional text-replacement presets that can be
    added to an instruction set, including a suggested default-active flag
    per entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403]:
    """ List replacement presets

     Returns the catalogue of optional text-replacement presets that can be
    added to an instruction set, including a suggested default-active flag
    per entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403]
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

) -> InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403 | None:
    """ List replacement presets

     Returns the catalogue of optional text-replacement presets that can be
    added to an instruction set, including a suggested default-active flag
    per entry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetReplacementPresetsResponse200 | InstructionSetReplacementPresetsResponse401 | InstructionSetReplacementPresetsResponse403
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
