from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.instruction_set_update_response_200 import InstructionSetUpdateResponse200
from ...models.instruction_set_update_response_401 import InstructionSetUpdateResponse401
from ...models.instruction_set_update_response_403 import InstructionSetUpdateResponse403
from ...models.instruction_set_update_response_404 import InstructionSetUpdateResponse404
from ...models.instruction_set_update_response_422 import InstructionSetUpdateResponse422
from ...models.update_instruction_set_request import UpdateInstructionSetRequest
from typing import cast



def _get_kwargs(
    instruction_set: str,
    *,
    body: UpdateInstructionSetRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/instruction-sets/{instruction_set}".format(instruction_set=quote(str(instruction_set), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = InstructionSetUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = InstructionSetUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = InstructionSetUpdateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = InstructionSetUpdateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = InstructionSetUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422]:
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
    body: UpdateInstructionSetRequest,

) -> Response[InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422]:
    """ Update an instruction set

     Updates the name, description, instructions and replacements of an
    instruction set belonging to the authenticated account. The submitted
    instructions and replacements replace the current lists – items absent
    from the payload are removed.

    Args:
        instruction_set (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateInstructionSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422]
     """


    kwargs = _get_kwargs(
        instruction_set=instruction_set,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    instruction_set: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInstructionSetRequest,

) -> InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422 | None:
    """ Update an instruction set

     Updates the name, description, instructions and replacements of an
    instruction set belonging to the authenticated account. The submitted
    instructions and replacements replace the current lists – items absent
    from the payload are removed.

    Args:
        instruction_set (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateInstructionSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422
     """


    return sync_detailed(
        instruction_set=instruction_set,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    instruction_set: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInstructionSetRequest,

) -> Response[InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422]:
    """ Update an instruction set

     Updates the name, description, instructions and replacements of an
    instruction set belonging to the authenticated account. The submitted
    instructions and replacements replace the current lists – items absent
    from the payload are removed.

    Args:
        instruction_set (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateInstructionSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422]
     """


    kwargs = _get_kwargs(
        instruction_set=instruction_set,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    instruction_set: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateInstructionSetRequest,

) -> InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422 | None:
    """ Update an instruction set

     Updates the name, description, instructions and replacements of an
    instruction set belonging to the authenticated account. The submitted
    instructions and replacements replace the current lists – items absent
    from the payload are removed.

    Args:
        instruction_set (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateInstructionSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstructionSetUpdateResponse200 | InstructionSetUpdateResponse401 | InstructionSetUpdateResponse403 | InstructionSetUpdateResponse404 | InstructionSetUpdateResponse422
     """


    return (await asyncio_detailed(
        instruction_set=instruction_set,
client=client,
body=body,

    )).parsed
