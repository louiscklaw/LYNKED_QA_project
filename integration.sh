#!/usr/bin/env bash

set -ex

./scripts/clear_report_directory.sh
rm -rf .pytest_cache

mkdir -p reports/functional/test_viewport/food
mkdir -p reports/functional/test_viewport/manage
mkdir -p reports/UI_test/functional/test_happyflow_1/result

pipenv sync

pipenv run pytest --maxfail=999 --json-report  --html=reports/functional/report.html -x tests/UI_test/functional/smoke_test
