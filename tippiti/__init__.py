"""Official Python client for the Tippiti API.

All resource IDs used with this client are sqid-encoded strings prefixed
with ``aid-`` (for example ``aid-xyz12345``). Raw integer IDs are rejected
with a 404 response by the server.
"""

from __future__ import annotations

from typing import Any

from tippiti.generated import AuthenticatedClient, Client

__all__ = [
    "Tippiti",
    "AuthenticatedClient",
    "Client",
]

DEFAULT_BASE_URL = "https://app.tippiti.io/api"


class Tippiti:
    """Factory for authenticated Tippiti API clients.

    Parameters
    ----------
    token:
        API token (Bearer credential).
    base_url:
        Override the API base URL. Defaults to ``https://app.tippiti.io/api``.
    headers:
        Extra HTTP headers to add to every request. The ``Authorization``
        header is managed by the client (always derived from ``token``) and
        cannot be overridden. ``Accept`` defaults to ``application/json`` but
        may be overridden here if needed.
    **httpx_kwargs:
        Extra keyword arguments forwarded to the underlying ``httpx.Client``
        constructor (e.g. ``timeout``, ``proxy``, ``verify``). Passing
        ``headers`` here is not supported; use the ``headers`` parameter above.
    """

    @staticmethod
    def create(
        token: str,
        base_url: str = DEFAULT_BASE_URL,
        headers: dict[str, str] | None = None,
        **httpx_kwargs: Any,
    ) -> AuthenticatedClient:
        if "headers" in httpx_kwargs:
            raise TypeError(
                "Pass custom headers via the 'headers' parameter, not as an "
                "httpx keyword argument."
            )

        merged_headers = {"Accept": "application/json"}
        if headers:
            merged_headers.update(headers)

        return AuthenticatedClient(
            base_url=base_url,
            token=token,
            headers=merged_headers,
            httpx_args=httpx_kwargs,
        )
