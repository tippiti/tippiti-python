from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_export_template_store_response_201 import DictationExportTemplateStoreResponse201
from ...models.dictation_export_template_store_response_401 import DictationExportTemplateStoreResponse401
from ...models.dictation_export_template_store_response_403 import DictationExportTemplateStoreResponse403
from ...models.dictation_export_template_store_response_422 import DictationExportTemplateStoreResponse422
from ...models.dictation_export_template_store_response_500 import DictationExportTemplateStoreResponse500
from ...models.upload_dictation_export_template_request import UploadDictationExportTemplateRequest
from typing import cast



def _get_kwargs(
    *,
    body: UploadDictationExportTemplateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictation-export-templates",
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500 | None:
    if response.status_code == 201:
        response_201 = DictationExportTemplateStoreResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = DictationExportTemplateStoreResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationExportTemplateStoreResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = DictationExportTemplateStoreResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DictationExportTemplateStoreResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadDictationExportTemplateRequest,

) -> Response[DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500]:
    """ Upload a Word export template

     Uploads a `.docx` file as a reusable export template. An optional
    `name` may be supplied; if omitted the file name is used. Main users
    may additionally set `is_shared_with_subusers` and pin the template
    to folders via `folder_ids`; for sub-users those fields are ignored.

    Args:
        body (UploadDictationExportTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UploadDictationExportTemplateRequest,

) -> DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500 | None:
    """ Upload a Word export template

     Uploads a `.docx` file as a reusable export template. An optional
    `name` may be supplied; if omitted the file name is used. Main users
    may additionally set `is_shared_with_subusers` and pin the template
    to folders via `folder_ids`; for sub-users those fields are ignored.

    Args:
        body (UploadDictationExportTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadDictationExportTemplateRequest,

) -> Response[DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500]:
    """ Upload a Word export template

     Uploads a `.docx` file as a reusable export template. An optional
    `name` may be supplied; if omitted the file name is used. Main users
    may additionally set `is_shared_with_subusers` and pin the template
    to folders via `folder_ids`; for sub-users those fields are ignored.

    Args:
        body (UploadDictationExportTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadDictationExportTemplateRequest,

) -> DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500 | None:
    """ Upload a Word export template

     Uploads a `.docx` file as a reusable export template. An optional
    `name` may be supplied; if omitted the file name is used. Main users
    may additionally set `is_shared_with_subusers` and pin the template
    to folders via `folder_ids`; for sub-users those fields are ignored.

    Args:
        body (UploadDictationExportTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportTemplateStoreResponse201 | DictationExportTemplateStoreResponse401 | DictationExportTemplateStoreResponse403 | DictationExportTemplateStoreResponse422 | DictationExportTemplateStoreResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
