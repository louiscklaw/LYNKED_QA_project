#!/usr/bin/env bash

set -ex


rsync -avzh --progress ./tests /home/logic/_workspace/LynkedKK_QA_test_scripts/tests
