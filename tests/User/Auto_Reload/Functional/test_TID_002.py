import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *

from create_appium_instance import *
from assert_check_point import *
from close_appium_session import *

from test_TID_001 import *
from check_TID_002 import *

def tour_TID_002(json_metadata):
  browser = tour_TID_001(json_metadata)

  browser = run_check(json_metadata, browser)

  return browser
