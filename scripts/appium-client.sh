#!/usr/bin/env bash

set -ex

appium -U emulator-5554 \
  -p 4723 \
  -bp 4724 \
  --chromedriver-port 8100 \
  --chromedriver-executable /home/logic/_workspace/LYNKED_QA_project/drivers/chrome/86/chromedriver
