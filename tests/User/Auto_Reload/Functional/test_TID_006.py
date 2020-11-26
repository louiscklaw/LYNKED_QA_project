import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_003 import tour_TID_003 as tour_TID_003
import lib.checks.check_TID_006 as check_TID_006

def test_TID_006(json_metadata):
  browser = tour_TID_003(json_metadata)

  # check result
  check_TID_006.run_check(json_metadata, browser)

  return browser