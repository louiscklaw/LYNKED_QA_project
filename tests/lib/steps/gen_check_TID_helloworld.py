#!/usr/bin/env python3

import os,sys
from pprint import pprint
from subprocess import run

HELLOWORLD_FILENAME='/home/logic/_workspace/LYNKED_QA_project/tests/lib/steps/check_TID_helloworld.py'

def getTargetFilename(idx):
  return HELLOWORLD_FILENAME.replace('check_TID_helloworld','check_TID_{:03.0f}'.format(idx))


for i in range(22, 30+1):
  print(run('cp {} {}'.format(
    HELLOWORLD_FILENAME,
    getTargetFilename(i)
  ), shell=True))
