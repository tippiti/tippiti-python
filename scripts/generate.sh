#!/usr/bin/env bash
set -euo pipefail

SPEC_URL="${TIPPITI_OPENAPI_URL:-https://apidocs.tippiti.io/api.json}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${ROOT_DIR}/tippiti/generated"

cd "${ROOT_DIR}"

if ! command -v openapi-python-client >/dev/null 2>&1; then
    echo "openapi-python-client not found. Install with: pip install openapi-python-client" >&2
    exit 1
fi

TMP_OUTPUT="$(mktemp -d)"
trap 'rm -rf "${TMP_OUTPUT}"' EXIT

openapi-python-client generate \
    --url "${SPEC_URL}" \
    --output-path "${TMP_OUTPUT}/out" \
    --overwrite \
    --config "${ROOT_DIR}/scripts/openapi-client.yaml"

# openapi-python-client emits `out/tippiti_client/` (depth 1). -maxdepth 2
# gives a small buffer for generator layout changes
PACKAGE_DIR=$(find "${TMP_OUTPUT}/out" -maxdepth 2 -type d -name "tippiti_client" -print -quit)

if [[ -z "${PACKAGE_DIR}" ]]; then
    echo "Generator did not produce the expected 'tippiti_client' package." >&2
    exit 1
fi

rm -rf "${TARGET_DIR}"
mkdir -p "${TARGET_DIR}"
cp -R "${PACKAGE_DIR}/." "${TARGET_DIR}/"

echo "Regenerated ${TARGET_DIR} from ${SPEC_URL}"
