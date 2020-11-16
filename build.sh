#!/usr/bin/env bash

set -ex

sh docs/flows/test_site_flows/build.sh

sh ./tests/UI_test/test.sh
