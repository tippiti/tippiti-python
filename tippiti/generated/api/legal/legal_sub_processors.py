from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.legal_sub_processors_response_200 import LegalSubProcessorsResponse200
from ...models.legal_sub_processors_response_401 import LegalSubProcessorsResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/legal/sub-processors",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401 | None:
    if response.status_code == 200:
        response_200 = LegalSubProcessorsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = LegalSubProcessorsResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401]:
    """ List sub-processors

     Returns the list of sub-processors engaged for service delivery. Each
    entry contains the company name, processing purpose, location and,
    where applicable, the transfer guarantee under GDPR. Authentication
    is required; the list is the same for all accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401]
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

) -> LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401 | None:
    """ List sub-processors

     Returns the list of sub-processors engaged for service delivery. Each
    entry contains the company name, processing purpose, location and,
    where applicable, the transfer guarantee under GDPR. Authentication
    is required; the list is the same for all accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401]:
    """ List sub-processors

     Returns the list of sub-processors engaged for service delivery. Each
    entry contains the company name, processing purpose, location and,
    where applicable, the transfer guarantee under GDPR. Authentication
    is required; the list is the same for all accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401]
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

) -> LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401 | None:
    """ List sub-processors

     Returns the list of sub-processors engaged for service delivery. Each
    entry contains the company name, processing purpose, location and,
    where applicable, the transfer guarantee under GDPR. Authentication
    is required; the list is the same for all accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LegalSubProcessorsResponse200 | LegalSubProcessorsResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
