from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auto_topup_update_body import AutoTopupUpdateBody
from ...models.auto_topup_update_response_200 import AutoTopupUpdateResponse200
from ...models.auto_topup_update_response_401 import AutoTopupUpdateResponse401
from ...models.auto_topup_update_response_422 import AutoTopupUpdateResponse422
from typing import cast



def _get_kwargs(
    *,
    body: AutoTopupUpdateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/billing/auto-topup",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = AutoTopupUpdateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = AutoTopupUpdateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = AutoTopupUpdateResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AutoTopupUpdateBody,

) -> Response[AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422]:
    """ Update auto top-up settings

     Updates the authenticated main user's auto top-up configuration.
    `enabled` is required; `threshold` (minimum balance in characters),
    `amount` (top-up amount in EUR, not below the pricing minimum) and
    `payment_method_id` (must belong to the account) are optional. Returns
    the updated settings. Main users only.

    Args:
        body (AutoTopupUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422]
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
    body: AutoTopupUpdateBody,

) -> AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422 | None:
    """ Update auto top-up settings

     Updates the authenticated main user's auto top-up configuration.
    `enabled` is required; `threshold` (minimum balance in characters),
    `amount` (top-up amount in EUR, not below the pricing minimum) and
    `payment_method_id` (must belong to the account) are optional. Returns
    the updated settings. Main users only.

    Args:
        body (AutoTopupUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AutoTopupUpdateBody,

) -> Response[AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422]:
    """ Update auto top-up settings

     Updates the authenticated main user's auto top-up configuration.
    `enabled` is required; `threshold` (minimum balance in characters),
    `amount` (top-up amount in EUR, not below the pricing minimum) and
    `payment_method_id` (must belong to the account) are optional. Returns
    the updated settings. Main users only.

    Args:
        body (AutoTopupUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422]
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
    body: AutoTopupUpdateBody,

) -> AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422 | None:
    """ Update auto top-up settings

     Updates the authenticated main user's auto top-up configuration.
    `enabled` is required; `threshold` (minimum balance in characters),
    `amount` (top-up amount in EUR, not below the pricing minimum) and
    `payment_method_id` (must belong to the account) are optional. Returns
    the updated settings. Main users only.

    Args:
        body (AutoTopupUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoTopupUpdateResponse200 | AutoTopupUpdateResponse401 | AutoTopupUpdateResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
