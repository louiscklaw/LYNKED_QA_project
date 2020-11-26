import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_014 import tour_TID_014 as tour_TID_014
import lib.checks.check_TID_015 as check_TID_015

def test_TID_015(json_metadata, username="TID_015"):

  browser = tour_TID_014(json_metadata, username)

  # the update of line up info appears here
  check_TID_015.run_check(json_metadata, browser)

  return browser
