#!/usr/bin/env python3

import os,sys
from pprint import pprint
from subprocess import run

HELLOWORLD_FILENAME='/home/logic/_workspace/LYNKED_QA_project/tests/lib/steps/check_TID_helloworld.py'

def getTargetFilename(idx):
  return HELLOWORLD_FILENAME.replace('check_TID_helloworld.py','check_TID_{:03.0f}.py'.format(idx))


def replaceTestNumber(str_in, find_text, replace_text):
  return str_in.replace(find_text, replace_text)

for i in range(30, 31+10+1):
  filename=getTargetFilename(i)
  print(run('cp {} {}'.format(
    HELLOWORLD_FILENAME,
    filename
  ), shell=True))

  fi=open(filename,'r')
  temp = fi.readlines()
  temp = map(lambda x: replaceTestNumber(x, 'TID_019','TID_{:03.0f}'.format(i)), temp)
  fi.close()

  fo=open(filename,'w')
  fo.writelines(temp)
  fo.close()