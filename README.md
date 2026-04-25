# Tippiti Python Client

Official Python client for the [Tippiti](https://tippiti.io) API – the transcription and dictation platform for physicians, attorneys, forensic examiners and professional typing services.

- **Interactive API docs:** [apidocs.tippiti.io](https://apidocs.tippiti.io)
- **OpenAPI specification:** [tippiti/openapi](https://github.com/tippiti/openapi)
- **Platform:** [tippiti.io](https://tippiti.io)
- **Support:** [app.tippiti.io/support/create](https://app.tippiti.io/support/create)

## Installation

```bash
pip install tippiti
```

Requires Python 3.10 or newer. Built on [httpx](https://www.python-httpx.org/) with type-annotated request and response models.

## Quick start

```python
import os

from tippiti import Tippiti
from tippiti.generated.api.dictation import dictation_index
from tippiti.generated.models.dictation_index_response_200 import (
    DictationIndexResponse200,
)

client = Tippiti.create(token=os.environ["TIPPITI_TOKEN"])

result = dictation_index.sync(client=client, include_notes=True)

if isinstance(result, DictationIndexResponse200):
    for dictation in result.data:
        print(dictation.id, dictation.title)
```

The `.sync()` helper returns the parsed payload directly; its return type is a union of all documented response models (`DictationIndexResponse200`, `DictationIndexResponse401`, `DictationIndexResponse422`, …). Narrow with `isinstance()` before touching model-specific fields, or use `.sync_detailed()` if you need the raw response (status code, headers, unparsed body). Every endpoint, parameter, and response is typed, derived directly from the OpenAPI specification at [apidocs.tippiti.io](https://apidocs.tippiti.io).

### Async variants

Every endpoint also ships an `asyncio` variant. Swap `.sync(...)` for `.asyncio(...)` (or `.sync_detailed(...)` for `.asyncio_detailed(...)`):

```python
import asyncio

async def main() -> None:
    result = await dictation_index.asyncio(client=client, include_notes=True)
    if isinstance(result, DictationIndexResponse200):
        for dictation in result.data:
            print(dictation.id, dictation.title)

asyncio.run(main())
```

## Authentication

The client sends your token as a `Bearer` credential in the `Authorization` header. Tokens are scoped to the issuing user's permissions (main user or sub-user with the relevant capabilities) and can be created in the account settings.

## Resource IDs

All resource identifiers are sqid-encoded strings prefixed with `aid-`, for example `aid-xyz12345`. Model fields reflect this – IDs are typed `str`, never `int`:

```python
from tippiti.generated.api.dictation import dictation_show

response = dictation_show.sync_detailed(client=client, dictation="aid-xyz12345")
```

Raw integer IDs are rejected with a `404` response.

## Available API modules

After installation, every API group has a dedicated module under `tippiti.generated.api.*`:

```python
from tippiti.generated.api.dictation import dictation_index, dictation_show, dictation_store
from tippiti.generated.api.folder import folder_index, folder_store
from tippiti.generated.api.account import account_show, account_update
from tippiti.generated.api.instruction_set import instruction_set_index
from tippiti.generated.api.sub_user import sub_user_index
# ...
```

Module and function names follow the tags and operationIds from the specification. See [apidocs.tippiti.io](https://apidocs.tippiti.io) for the full operation list.

## Response envelope

`.sync()` / `.asyncio()` return a typed dataclass exposing `success` and either `data` (success) or `message` / `errors` (failure). `.sync_detailed()` / `.asyncio_detailed()` wrap that payload in a `Response` object whose `.parsed` attribute is typed as a union of all possible status-code responses – use `response.status_code` to pick the right branch. Validation failures return `422` with per-field error messages. Rate-limit breaches return `429` with a `Retry-After` header.

## Custom base URL

```python
client = Tippiti.create(
    token="...",
    base_url="https://staging.app.tippiti.io/api",
)
```

## Custom httpx configuration

Pass any keyword argument to `Tippiti.create(...)` and it is forwarded to the underlying httpx client – for example `timeout`, `proxy`, or TLS settings:

```python
client = Tippiti.create(
    token="...",
    timeout=30.0,
    follow_redirects=True,
)
```

## Versioning

This client follows [Semantic Versioning](https://semver.org). A release note in [CHANGELOG.md](CHANGELOG.md) accompanies every version. Breaking changes to the underlying API produce a major version bump of this package.

## License

[MIT](LICENSE). The Tippiti platform, trademarks and data are not covered by this license.
