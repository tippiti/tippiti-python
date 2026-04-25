from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.instruction_set_index_response_200 import InstructionSetIndexResponse200
from ...models.instruction_set_index_response_401 import InstructionSetIndexResponse401
from ...models.instruction_set_index_response_403 import InstructionSetIndexResponse403
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/instruction-sets",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403 | None:
    if response.status_code == 200:
        response_200 = InstructionSetIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = InstructionSetIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InstructionSetIndexResponse403.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403]:
    """ List instruction sets

     Returns all dictation instruction sets belonging to the authenticated
    account, including their instructions and text replacements. The
    default set is returned first, followed by the remainder ordered by
    name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403]
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

) -> InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403 | None:
    """ List instruction sets

     Returns all dictation instruction sets belonging to the authenticated
    account, including their instructions and text replacements. The
    default set is returned first, followed by the remainder ordered by
    name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403]:
    """ List instruction sets

     Returns all dictation instruction sets belonging to the authenticated
    account, including their instructions and text replacements. The
    default set is returned first, followed by the remainder ordered by
    name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403]
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

) -> InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403 | None:
    """ List instruction sets

     Returns all dictation instruction sets belonging to the authenticated
    account, including their instructions and text replacements. The
    default set is returned first, followed by the remainder ordered by
    name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetIndexResponse200 | InstructionSetIndexResponse401 | InstructionSetIndexResponse403
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
