from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_export_template_destroy_response_200 import DictationExportTemplateDestroyResponse200
from ...models.dictation_export_template_destroy_response_401 import DictationExportTemplateDestroyResponse401
from ...models.dictation_export_template_destroy_response_403 import DictationExportTemplateDestroyResponse403
from ...models.dictation_export_template_destroy_response_404 import DictationExportTemplateDestroyResponse404
from typing import cast



def _get_kwargs(
    template: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/dictation-export-templates/{template}".format(template=quote(str(template), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404 | None:
    if response.status_code == 200:
        response_200 = DictationExportTemplateDestroyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DictationExportTemplateDestroyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationExportTemplateDestroyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationExportTemplateDestroyResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404]:
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

) -> Response[DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404]:
    """ Delete a Word export template

     Removes the template record and its stored file. Only the owner may
    delete a template.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404]
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

) -> DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404 | None:
    """ Delete a Word export template

     Removes the template record and its stored file. Only the owner may
    delete a template.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404
     """


    return sync_detailed(
        template=template,
client=client,

    ).parsed

async def asyncio_detailed(
    template: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404]:
    """ Delete a Word export template

     Removes the template record and its stored file. Only the owner may
    delete a template.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404]
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

) -> DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404 | None:
    """ Delete a Word export template

     Removes the template record and its stored file. Only the owner may
    delete a template.

    Args:
        template (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportTemplateDestroyResponse200 | DictationExportTemplateDestroyResponse401 | DictationExportTemplateDestroyResponse403 | DictationExportTemplateDestroyResponse404
     """


    return (await asyncio_detailed(
        template=template,
client=client,

    )).parsed
