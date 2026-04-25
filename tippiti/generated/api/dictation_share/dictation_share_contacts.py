from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_share_contacts_response_200 import DictationShareContactsResponse200
from ...models.dictation_share_contacts_response_401 import DictationShareContactsResponse401
from ...models.dictation_share_contacts_response_403 import DictationShareContactsResponse403
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/shares/contacts",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403 | None:
    if response.status_code == 200:
        response_200 = DictationShareContactsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationShareContactsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationShareContactsResponse403.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403]:
    """ List previously used share recipients

     Returns the distinct, alphabetically sorted list of email addresses
    the account has previously sent share links to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403]
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

) -> DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403 | None:
    """ List previously used share recipients

     Returns the distinct, alphabetically sorted list of email addresses
    the account has previously sent share links to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403]:
    """ List previously used share recipients

     Returns the distinct, alphabetically sorted list of email addresses
    the account has previously sent share links to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403]
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

) -> DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403 | None:
    """ List previously used share recipients

     Returns the distinct, alphabetically sorted list of email addresses
    the account has previously sent share links to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationShareContactsResponse200 | DictationShareContactsResponse401 | DictationShareContactsResponse403
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
