#!/usr/bin/env bash

set -ex

pipenv run pytest tests/UI_test/functional/test_helloworld.py
pipenv run pytest tests/UI_test/new_feature/test_helloworld.py
pipenv run pytest tests/UI_test/regression/test_helloworld.py
