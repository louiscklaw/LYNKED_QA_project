import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_026 import tour_TID_026 as tour_TID_026
import lib.checks.check_TID_027 as check_TID_027

def test_TID_027(json_metadata):
  password_to_bruce=['xxxxxx']

  restaurant_manage_browser = tour_TID_026(json_metadata)

  for password in password_to_bruce:
    check_TID_027.run_check(json_metadata, restaurant_manage_browser, password)

  restaurant_manage_browser.quit()

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')