#!/usr/bin/env bash

set -ex

appium -U emulator-5556 \
  -p 5723 \
  -bp 5724 \
  --chromedriver-port 8101 \
  --chromedriver-executable /home/logic/_workspace/LYNKED_QA_project/drivers/chrome/74/chromedriver
