#!/usr/bin/env bash

set -ex

pipenv run pytest --html=docs/functional/report.html tests/UI_test/functional/test_helloworld.py
pipenv run pytest --html=docs/new_feature/report.html tests/UI_test/new_feature/test_helloworld.py
pipenv run pytest --html=docs/regression/report.html tests/UI_test/regression/test_helloworld.py
