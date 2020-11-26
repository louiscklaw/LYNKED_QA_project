import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *

from create_appium_instance import *
from assert_check_point import *
from close_appium_session import *

from test_TID_002 import *
import check_TID_003

def test_TID_003(json_metadata):
  browser = tour_TID_002(json_metadata)

  browser = check_TID_003.run_check(json_metadata, browser)

  return browser
