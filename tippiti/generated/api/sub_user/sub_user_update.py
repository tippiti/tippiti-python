from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.sub_user_update_response_200 import SubUserUpdateResponse200
from ...models.sub_user_update_response_401 import SubUserUpdateResponse401
from ...models.sub_user_update_response_403 import SubUserUpdateResponse403
from ...models.sub_user_update_response_404 import SubUserUpdateResponse404
from ...models.sub_user_update_response_422 import SubUserUpdateResponse422
from ...models.update_sub_user_request import UpdateSubUserRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    sub_user: str,
    *,
    body: UpdateSubUserRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/sub-users/{sub_user}".format(sub_user=quote(str(sub_user), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = SubUserUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = SubUserUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SubUserUpdateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SubUserUpdateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = SubUserUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sub_user: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSubUserRequest | Unset = UNSET,

) -> Response[SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422]:
    """ Update a sub-user

     Updates profile fields (name, email, active flag) and/or the permission
    profile of a sub-user owned by the authenticated main user. Permission
    fields are only applied when supplied. Main users only.

    Args:
        sub_user (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateSubUserRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422]
     """


    kwargs = _get_kwargs(
        sub_user=sub_user,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    sub_user: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSubUserRequest | Unset = UNSET,

) -> SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422 | None:
    """ Update a sub-user

     Updates profile fields (name, email, active flag) and/or the permission
    profile of a sub-user owned by the authenticated main user. Permission
    fields are only applied when supplied. Main users only.

    Args:
        sub_user (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateSubUserRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422
     """


    return sync_detailed(
        sub_user=sub_user,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    sub_user: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSubUserRequest | Unset = UNSET,

) -> Response[SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422]:
    """ Update a sub-user

     Updates profile fields (name, email, active flag) and/or the permission
    profile of a sub-user owned by the authenticated main user. Permission
    fields are only applied when supplied. Main users only.

    Args:
        sub_user (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateSubUserRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422]
     """


    kwargs = _get_kwargs(
        sub_user=sub_user,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    sub_user: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSubUserRequest | Unset = UNSET,

) -> SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422 | None:
    """ Update a sub-user

     Updates profile fields (name, email, active flag) and/or the permission
    profile of a sub-user owned by the authenticated main user. Permission
    fields are only applied when supplied. Main users only.

    Args:
        sub_user (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateSubUserRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubUserUpdateResponse200 | SubUserUpdateResponse401 | SubUserUpdateResponse403 | SubUserUpdateResponse404 | SubUserUpdateResponse422
     """


    return (await asyncio_detailed(
        sub_user=sub_user,
client=client,
body=body,

    )).parsed
