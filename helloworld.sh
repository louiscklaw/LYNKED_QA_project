#!/usr/bin/env bash

set -ex

# function shutdown {
#     ./scripts/down_docker_selenium.sh
#     echo "Shutdown complete"
# }

# trap shutdown SIGTERM SIGINT EXIT

./scripts/clear_report_directory.sh
rm -rf .pytest_cache

mkdir -p reports/functional/test_viewport/food
mkdir -p reports/functional/test_viewport/manage
mkdir -p reports/UI_test/functional/test_happyflow_1/result

# touch reports/functional/test_viewport/food/.gitkeep
# touch reports/functional/test_viewport/manage/.gitkeep

sudo rm -rf /home/logic/_workspace/LYNKED_QA_project/_ref/docker-appium/video-nexus_10/*

pipenv run pytest --maxfail=999 --json-report  --html=tests/User/reports/report.html -x tests/User/helloworlds
# pipenv run pytest --maxfail=999 --json-report  --html=tests/User/reports/report.html -x tests/User/helloworlds
