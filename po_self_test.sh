#!/usr/bin/env bash

set -ex

pipenv run pytest --capture=sys tests/po_tests/test_main.py
