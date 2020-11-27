import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_023 import tour_TID_023 as tour_TID_023
import lib.checks.check_TID_009 as check_TID_009

def test_TID_025(json_metadata, username="TID_025"):
  browser = tour_TID_023(json_metadata, username)

  for i in range(1, NUM_PEOPLE_TOTAL+1):
    check_TID_025.run_check(json_metadata, browser,i)

  return browser
