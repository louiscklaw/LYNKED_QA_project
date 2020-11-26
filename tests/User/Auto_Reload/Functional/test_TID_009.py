import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_006 import tour_TID_006 as tour_TID_006
import lib.checks.check_TID_009 as check_TID_009

def tour_TID_009(json_metadata, username="TID_009"):

  browser = tour_TID_006(json_metadata, username)

  # the update of line up info appears here
  check_TID_009.run_check(json_metadata, browser)

  return browser
