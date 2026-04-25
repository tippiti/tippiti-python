from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.faq_article_support_response_200 import FaqArticleSupportResponse200
from ...models.faq_article_support_response_401 import FaqArticleSupportResponse401
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/support/faq",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FaqArticleSupportResponse200 | FaqArticleSupportResponse401 | None:
    if response.status_code == 200:
        response_200 = FaqArticleSupportResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = FaqArticleSupportResponse401.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FaqArticleSupportResponse200 | FaqArticleSupportResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[FaqArticleSupportResponse200 | FaqArticleSupportResponse401]:
    """ List support-area FAQ articles

     Returns the active FAQ articles published for the support area,
    ordered for display. Available to main users and to sub-users with
    the support-access capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FaqArticleSupportResponse200 | FaqArticleSupportResponse401]
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

) -> FaqArticleSupportResponse200 | FaqArticleSupportResponse401 | None:
    """ List support-area FAQ articles

     Returns the active FAQ articles published for the support area,
    ordered for display. Available to main users and to sub-users with
    the support-access capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FaqArticleSupportResponse200 | FaqArticleSupportResponse401
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[FaqArticleSupportResponse200 | FaqArticleSupportResponse401]:
    """ List support-area FAQ articles

     Returns the active FAQ articles published for the support area,
    ordered for display. Available to main users and to sub-users with
    the support-access capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FaqArticleSupportResponse200 | FaqArticleSupportResponse401]
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

) -> FaqArticleSupportResponse200 | FaqArticleSupportResponse401 | None:
    """ List support-area FAQ articles

     Returns the active FAQ articles published for the support area,
    ordered for display. Available to main users and to sub-users with
    the support-access capability.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FaqArticleSupportResponse200 | FaqArticleSupportResponse401
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
