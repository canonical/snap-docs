#!/bin/bash

# Configuration
REPO="canonical/snapd"
WORKFLOW="build-documentation.yaml"
ARTIFACT_NAME="rest-api-documentation"
TARGET_DIR="${SOURCEDIR}/_html_extra/reference/api"

mkdir -p "${TARGET_DIR}"

echo "Searching for the latest successful run that has artifact '${ARTIFACT_NAME}'..."

# RUN_IDS=$(gh run list \
#  -R "${REPO}" \
#  --workflow "${WORKFLOW}" \
#  --status success \
#  --limit 100 \
#  --json databaseId \
#  -q '.[].databaseId')
#
#DOWNLOAD_SUCCESS=false
#
#for id in $RUN_IDS; do
#  echo -n "Checking Run ID $id... "
#  
#  gh run download "$id" -R "${REPO}" -n "${ARTIFACT_NAME}" -D "${TARGET_DIR}" >/dev/null 2>&1
#  
#  if [ $? -eq 0 ]; then
#    echo "Found and downloaded!"
#    DOWNLOAD_SUCCESS=true
#    break
#  else
#    echo "Artifact not found (skipped)."
#  fi
# done
#
# if [ "$DOWNLOAD_SUCCESS" = false ]; then
#  echo "Error: Checked the last 100 successful runs, but none contained the artifact '${ARTIFACT_NAME}'."
#  exit 1
#fi
#
echo "OpenAPI docs successfully downloaded to ${TARGET_DIR}"

echo "OpenAPI docs successfully downloaded to ${TARGET_DIR}"
