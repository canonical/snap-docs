#!/bin/bash

# Configuration
REPO="canonical/snapd"
WORKFLOW="build-documentation.yaml"
ARTIFACT_NAME="rest-api-documentation"
TARGET_DIR="${SOURCEDIR}/_html_extra/reference/api"

mkdir -p "${TARGET_DIR}"

echo "Fetching latest successful Run ID from ${REPO} (branch: master)..."

# Logic:
# 1. List the last 20 runs (to provide a buffer in case the last few failed).
# 2. Fetch specific JSON fields: databaseId, headBranch, and conclusion.
# 3. Use -q (jq query) to filter for runs where branch is 'master' AND result is 'success'.
# 4. Use head -n 1 to grab the very top (newest) result from that filtered list.
LATEST_RUN_ID=$(gh run list \
  -R "${REPO}" \
  --workflow "${WORKFLOW}" \
  --status success \
  --json databaseId,headBranch,conclusion \
  -q '.[] | select(.headBranch == "master") | .databaseId' \
  | head -n 1)

if [ -z "$LATEST_RUN_ID" ]; then
  echo "Error: Could not find a successful run on branch 'master' within the last 20 attempts."
  exit 1
fi

echo "Found latest successful Run ID: $LATEST_RUN_ID"

echo "Downloading artifact '${ARTIFACT_NAME}'..."
gh run download "$LATEST_RUN_ID" -R "${REPO}" -n "${ARTIFACT_NAME}" -D "${TARGET_DIR}"
if [ $? -eq 0 ]; then
  echo "OpenAPI docs successfully downloaded to ${TARGET_DIR}"
else
  echo "Error: Failed to download artifacts."
  exit 1
fi
