from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_export_template_download_url_response_200 import DictationExportTemplateDownloadUrlResponse200
from ...models.dictation_export_template_download_url_response_401 import DictationExportTemplateDownloadUrlResponse401
from ...models.dictation_export_template_download_url_response_403 import DictationExportTemplateDownloadUrlResponse403
from ...models.dictation_export_template_download_url_response_404 import DictationExportTemplateDownloadUrlResponse404
from typing import cast



def _get_kwargs(
    template: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dictation-export-templates/{template}/download-url".format(template=quote(str(template), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationExportTemplateDownloadUrlResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationExportTemplateDownloadUrlResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationExportTemplateDownloadUrlResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationExportTemplateDownloadUrlResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404]:
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

) -> Response[DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404]:
    """ Get a download URL for a Word export template

     Returns a short-lived download URL for the template file. Requires
    the caller to have download rights on the template – main users on
    their own templates, sub-users on their own and on shared templates.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404]
     """


    kwargs = _get_kwargs(
        template=template,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    template: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404 | None:
    """ Get a download URL for a Word export template

     Returns a short-lived download URL for the template file. Requires
    the caller to have download rights on the template – main users on
    their own templates, sub-users on their own and on shared templates.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404
     """


    return sync_detailed(
        template=template,
client=client,

    ).parsed

async def asyncio_detailed(
    template: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404]:
    """ Get a download URL for a Word export template

     Returns a short-lived download URL for the template file. Requires
    the caller to have download rights on the template – main users on
    their own templates, sub-users on their own and on shared templates.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404]
     """


    kwargs = _get_kwargs(
        template=template,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    template: str,
    *,
    client: AuthenticatedClient | Client,

) -> DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404 | None:
    """ Get a download URL for a Word export template

     Returns a short-lived download URL for the template file. Requires
    the caller to have download rights on the template – main users on
    their own templates, sub-users on their own and on shared templates.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportTemplateDownloadUrlResponse200 | DictationExportTemplateDownloadUrlResponse401 | DictationExportTemplateDownloadUrlResponse403 | DictationExportTemplateDownloadUrlResponse404
     """


    return (await asyncio_detailed(
        template=template,
client=client,

    )).parsed
