import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_037 import tour_TID_037 as tour_TID_037
import lib.checks.check_TID_044 as check_TID_044

def tour_TID_044(json_metadata):
  # clear before test

  (r_browser, c_browser) = tour_TID_037(json_metadata, '44')

  # perform check
  check_TID_044.run_check(json_metadata, r_browser, 44)

  return (r_browser, c_browser)
