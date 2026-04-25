from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_export_template_update_response_200 import DictationExportTemplateUpdateResponse200
from ...models.dictation_export_template_update_response_401 import DictationExportTemplateUpdateResponse401
from ...models.dictation_export_template_update_response_403 import DictationExportTemplateUpdateResponse403
from ...models.dictation_export_template_update_response_404 import DictationExportTemplateUpdateResponse404
from ...models.dictation_export_template_update_response_422 import DictationExportTemplateUpdateResponse422
from ...models.update_dictation_export_template_request import UpdateDictationExportTemplateRequest
from typing import cast



def _get_kwargs(
    template: str,
    *,
    body: UpdateDictationExportTemplateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/dictation-export-templates/{template}".format(template=quote(str(template), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = DictationExportTemplateUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationExportTemplateUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationExportTemplateUpdateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationExportTemplateUpdateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationExportTemplateUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDictationExportTemplateRequest,

) -> Response[DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422]:
    """ Update a Word export template

     Renames the template and, for main users, updates sharing
    (`is_shared_with_subusers`) and folder pinning (`folder_ids`).
    Sharing and folder fields supplied by sub-users are ignored so that
    a simple rename still succeeds.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateDictationExportTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422]
     """


    kwargs = _get_kwargs(
        template=template,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    template: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDictationExportTemplateRequest,

) -> DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422 | None:
    """ Update a Word export template

     Renames the template and, for main users, updates sharing
    (`is_shared_with_subusers`) and folder pinning (`folder_ids`).
    Sharing and folder fields supplied by sub-users are ignored so that
    a simple rename still succeeds.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateDictationExportTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422
     """


    return sync_detailed(
        template=template,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    template: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDictationExportTemplateRequest,

) -> Response[DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422]:
    """ Update a Word export template

     Renames the template and, for main users, updates sharing
    (`is_shared_with_subusers`) and folder pinning (`folder_ids`).
    Sharing and folder fields supplied by sub-users are ignored so that
    a simple rename still succeeds.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateDictationExportTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422]
     """


    kwargs = _get_kwargs(
        template=template,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    template: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDictationExportTemplateRequest,

) -> DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422 | None:
    """ Update a Word export template

     Renames the template and, for main users, updates sharing
    (`is_shared_with_subusers`) and folder pinning (`folder_ids`).
    Sharing and folder fields supplied by sub-users are ignored so that
    a simple rename still succeeds.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (UpdateDictationExportTemplateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportTemplateUpdateResponse200 | DictationExportTemplateUpdateResponse401 | DictationExportTemplateUpdateResponse403 | DictationExportTemplateUpdateResponse404 | DictationExportTemplateUpdateResponse422
     """


    return (await asyncio_detailed(
        template=template,
client=client,
body=body,

    )).parsed
