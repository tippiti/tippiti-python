from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dictation_export_docx_body import DictationExportDocxBody
from ...models.dictation_export_docx_response_401 import DictationExportDocxResponse401
from ...models.dictation_export_docx_response_403 import DictationExportDocxResponse403
from ...models.dictation_export_docx_response_404 import DictationExportDocxResponse404
from ...models.dictation_export_docx_response_422 import DictationExportDocxResponse422
from typing import cast



def _get_kwargs(
    dictation: str,
    *,
    body: DictationExportDocxBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dictations/{dictation}/export/docx".format(dictation=quote(str(dictation), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422 | None:
    if response.status_code == 401:
        response_401 = DictationExportDocxResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DictationExportDocxResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DictationExportDocxResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DictationExportDocxResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422]:
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
    body: DictationExportDocxBody,

) -> Response[DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422]:
    """ Export a dictation as a DOCX file

     Renders the supplied `html` body into a Word document and streams it
    back to the caller. An optional `template_id` selects one of the
    caller's saved export templates whose styling is applied to the
    output, or a `reference` multipart upload can be provided for a
    one-time styled export. Without either parameter a default layout
    is used. Requires view access to the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationExportDocxBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422]
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
    body: DictationExportDocxBody,

) -> DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422 | None:
    """ Export a dictation as a DOCX file

     Renders the supplied `html` body into a Word document and streams it
    back to the caller. An optional `template_id` selects one of the
    caller's saved export templates whose styling is applied to the
    output, or a `reference` multipart upload can be provided for a
    one-time styled export. Without either parameter a default layout
    is used. Requires view access to the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationExportDocxBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422
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
    body: DictationExportDocxBody,

) -> Response[DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422]:
    """ Export a dictation as a DOCX file

     Renders the supplied `html` body into a Word document and streams it
    back to the caller. An optional `template_id` selects one of the
    caller's saved export templates whose styling is applied to the
    output, or a `reference` multipart upload can be provided for a
    one-time styled export. Without either parameter a default layout
    is used. Requires view access to the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationExportDocxBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422]
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
    body: DictationExportDocxBody,

) -> DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422 | None:
    """ Export a dictation as a DOCX file

     Renders the supplied `html` body into a Word document and streams it
    back to the caller. An optional `template_id` selects one of the
    caller's saved export templates whose styling is applied to the
    output, or a `reference` multipart upload can be provided for a
    one-time styled export. Without either parameter a default layout
    is used. Requires view access to the dictation.

    Args:
        dictation (str): Sqid-kodierte ID (Präfix `aid-`). Example: aid-xyz12345.
        body (DictationExportDocxBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictationExportDocxResponse401 | DictationExportDocxResponse403 | DictationExportDocxResponse404 | DictationExportDocxResponse422
     """


    return (await asyncio_detailed(
        dictation=dictation,
client=client,
body=body,

    )).parsed
