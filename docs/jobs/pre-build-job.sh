#!/bin/bash

# Configuration
REPO="canonical/snapd"
WORKFLOW="build-documentation.yaml" 
ARTIFACT_NAME="openapi-spec"
TARGET_DIR="${SOURCEDIR}/_html_extra/reference/api"
N_RUNS=100

mkdir -p "${TARGET_DIR}"

echo "Searching for the latest successful ${WORKFLOW} run that has artifact '${ARTIFACT_NAME}'..."

RUN_IDS=$(gh run list \
  -R "${REPO}" \
  --workflow "${WORKFLOW}" \
  --status success \
  --branch master \
  --limit "${N_RUNS}" \
  --json databaseId \
  -q '.[].databaseId')

if [ -z "$RUN_IDS" ]; then
  echo "Error: No successful runs found for '${WORKFLOW}' workflow from the master branch of '${REPO}' repo."
  exit 1
fi

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
  RUNS_FOUND=$(echo "$RUN_IDS" | wc -l)
  echo "Error: Checked the last ${RUNS_FOUND} successful runs, but none contained the artifact '${ARTIFACT_NAME}'."
  mv ${SOURCEDIR}/_html_extra/reference/development/snapd-rest-api/openapi.json ${TARGET_DIR}/openapi.json
  echo "Using local copy of openapi.json instead."
fi

echo "OpenAPI spec successfully downloaded to ${TARGET_DIR}/openapi.json"
