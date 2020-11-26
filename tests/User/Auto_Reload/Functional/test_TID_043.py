import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from Auto_Reload.Functional.test_TID_041 import tour_TID_041 as tour_TID_041
import lib.checks.check_TID_043 as check_TID_043

def test_TID_043(json_metadata, table_num=43, food_quantity=5):

  # clear before test
  (r_browser, c_browser) = tour_TID_041(json_metadata, table_num, food_quantity)

  check_TID_043.run_check(json_metadata, r_browser,  food_quantity-1)

  return (r_browser, c_browser)
