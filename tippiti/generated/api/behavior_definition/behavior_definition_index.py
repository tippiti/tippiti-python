from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.behavior_definition_index_response_200 import BehaviorDefinitionIndexResponse200
from ...models.behavior_definition_index_response_401 import BehaviorDefinitionIndexResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/behavior-definitions",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401 | None:
    if response.status_code == 200:
        response_200 = BehaviorDefinitionIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = BehaviorDefinitionIndexResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401]:
    """ List configurable behavior definitions

     Returns the configurable behavior definitions available to the
    authenticated account, each with its label, description, value type,
    default value, option list and the account's current effective value.
    Definitions that require a capability the caller does not hold are
    omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401]
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

) -> BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401 | None:
    """ List configurable behavior definitions

     Returns the configurable behavior definitions available to the
    authenticated account, each with its label, description, value type,
    default value, option list and the account's current effective value.
    Definitions that require a capability the caller does not hold are
    omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401]:
    """ List configurable behavior definitions

     Returns the configurable behavior definitions available to the
    authenticated account, each with its label, description, value type,
    default value, option list and the account's current effective value.
    Definitions that require a capability the caller does not hold are
    omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401]
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

) -> BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401 | None:
    """ List configurable behavior definitions

     Returns the configurable behavior definitions available to the
    authenticated account, each with its label, description, value type,
    default value, option list and the account's current effective value.
    Definitions that require a capability the caller does not hold are
    omitted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BehaviorDefinitionIndexResponse200 | BehaviorDefinitionIndexResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
