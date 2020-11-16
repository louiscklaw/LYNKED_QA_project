#!/usr/bin/env bash

set -ex

REPO_HOME=$(dirname $0)
PATH=$PATH:$REPO_HOME/drivers/chrome/85

sh docs/flows/test_site_flows/build.sh

# pipenv run pytest --html=docs/functional/report.html tests
pipenv run pytest --html=reports/regression/report.html tests/UI_test/regression
pipenv run pytest --html=reports/functional/report.html tests/UI_test/functional
pipenv run pytest --html=reports/new_feature/report.html tests/UI_test/new_feature
