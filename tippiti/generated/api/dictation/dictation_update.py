from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_update_body import DictationUpdateBody
from ...models.dictation_update_response_200 import DictationUpdateResponse200
from ...models.dictation_update_response_401 import DictationUpdateResponse401
from ...models.dictation_update_response_403 import DictationUpdateResponse403
from ...models.dictation_update_response_404 import DictationUpdateResponse404
from ...models.dictation_update_response_422 import DictationUpdateResponse422
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    dictation: str,
    *,
    body: DictationUpdateBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/dictations/{dictation}".format(dictation=quote(str(dictation), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationUpdateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationUpdateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationUpdateBody | Unset = UNSET,

) -> Response[DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422]:
    """ Update dictation metadata

     Updates the supplied metadata fields on an existing dictation. Title,
    client name and comment require the metadata-edit capability; folder
    assignment requires the folder capability; assigning an instruction
    set requires the instructions capability. Sharing a dictation with
    specific sub-users via `shared_with` is reserved for main users.
    Returns the updated dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationUpdateBody | Unset = UNSET,

) -> DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422 | None:
    """ Update dictation metadata

     Updates the supplied metadata fields on an existing dictation. Title,
    client name and comment require the metadata-edit capability; folder
    assignment requires the folder capability; assigning an instruction
    set requires the instructions capability. Sharing a dictation with
    specific sub-users via `shared_with` is reserved for main users.
    Returns the updated dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422
     """


    return sync_detailed(
        dictation=dictation,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationUpdateBody | Unset = UNSET,

) -> Response[DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422]:
    """ Update dictation metadata

     Updates the supplied metadata fields on an existing dictation. Title,
    client name and comment require the metadata-edit capability; folder
    assignment requires the folder capability; assigning an instruction
    set requires the instructions capability. Sharing a dictation with
    specific sub-users via `shared_with` is reserved for main users.
    Returns the updated dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422]
     """


    kwargs = _get_kwargs(
        dictation=dictation,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dictation: str,
    *,
    client: AuthenticatedClient | Client,
    body: DictationUpdateBody | Unset = UNSET,

) -> DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422 | None:
    """ Update dictation metadata

     Updates the supplied metadata fields on an existing dictation. Title,
    client name and comment require the metadata-edit capability; folder
    assignment requires the folder capability; assigning an instruction
    set requires the instructions capability. Sharing a dictation with
    specific sub-users via `shared_with` is reserved for main users.
    Returns the updated dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationUpdateBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationUpdateResponse200 | DictationUpdateResponse401 | DictationUpdateResponse403 | DictationUpdateResponse404 | DictationUpdateResponse422
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,
body=body,

    )).parsed
