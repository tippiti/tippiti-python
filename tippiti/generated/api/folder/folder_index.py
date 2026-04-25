from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.folder_index_response_200_type_0 import FolderIndexResponse200Type0
from ...models.folder_index_response_200_type_1 import FolderIndexResponse200Type1
from ...models.folder_index_response_200_type_2 import FolderIndexResponse200Type2
from ...models.folder_index_response_401 import FolderIndexResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/folders",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401 | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = FolderIndexResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = FolderIndexResponse200Type1.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = FolderIndexResponse200Type2.from_dict(data)



            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FolderIndexResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401]:
    """ List folders

     Returns the authenticated account's folder tree. Main users receive all
    own folders plus any folders referenced by sub-user access grants that
    are not part of the main tree. Sub-users receive only folders they are
    permitted to see based on their access mode; folders they cannot see
    are pruned from the hierarchy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401]
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

) -> FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401 | None:
    """ List folders

     Returns the authenticated account's folder tree. Main users receive all
    own folders plus any folders referenced by sub-user access grants that
    are not part of the main tree. Sub-users receive only folders they are
    permitted to see based on their access mode; folders they cannot see
    are pruned from the hierarchy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401]:
    """ List folders

     Returns the authenticated account's folder tree. Main users receive all
    own folders plus any folders referenced by sub-user access grants that
    are not part of the main tree. Sub-users receive only folders they are
    permitted to see based on their access mode; folders they cannot see
    are pruned from the hierarchy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401]
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

) -> FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401 | None:
    """ List folders

     Returns the authenticated account's folder tree. Main users receive all
    own folders plus any folders referenced by sub-user access grants that
    are not part of the main tree. Sub-users receive only folders they are
    permitted to see based on their access mode; folders they cannot see
    are pruned from the hierarchy.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FolderIndexResponse200Type0 | FolderIndexResponse200Type1 | FolderIndexResponse200Type2 | FolderIndexResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
