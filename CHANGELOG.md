# Changelog

All notable changes to the Tippiti Python client are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the package adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.2] – 2026-04-25

### Added

- Initial release of the official Python client.
- Type-annotated bindings for the Tippiti OpenAPI 3.1 specification, built on [httpx](https://www.python-httpx.org/) and [attrs](https://www.attrs.org/).
- `Tippiti.create()` factory with token authentication and custom base URL support.
- Synchronous and asynchronous (asyncio) request variants for every endpoint.
