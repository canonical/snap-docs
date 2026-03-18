#!/bin/bash

# Configuration
REPO="canonical/snap-docs"
WORKFLOW="build-rest-api.yml" 
ARTIFACT_NAME="openapi-spec"
TARGET_DIR="${SOURCEDIR}/_html_extra/reference/api"

mkdir -p "${TARGET_DIR}"

echo "Searching for the latest successful run that has artifact '${ARTIFACT_NAME}'..."

RUN_IDS=$(gh run list \
  -R "${REPO}" \
  --workflow "${WORKFLOW}" \
  --status success \
  --branch master \
  --limit 100 \
  --json databaseId \
  -q '.[].databaseId')

DOWNLOAD_SUCCESS=false

for id in $RUN_IDS; do
  echo -n "Checking Run ID $id... "
  
  # Download the artifact contents directly into the target directory
  gh run download "$id" -R "${REPO}" -n "${ARTIFACT_NAME}" -D "${TARGET_DIR}" >/dev/null 2>&1
  
  if [ $? -eq 0 ]; then
    echo "Found and downloaded!"
    DOWNLOAD_SUCCESS=true
    break
  else
    echo "Artifact not found (skipped)."
  fi
done

if [ "$DOWNLOAD_SUCCESS" = false ]; then
  echo "Error: Checked the last 100 successful runs, but none contained the artifact '${ARTIFACT_NAME}'."
  exit 1
fi

echo "OpenAPI spec successfully downloaded to ${TARGET_DIR}/openapi.json"
