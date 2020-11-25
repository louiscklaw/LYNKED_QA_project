import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *

from steps import *
from pages.config import *
from jp import *

from urls import *

from setupLocalChrome import *

from test_TID_039 import *

def test_TID_040(json_metadata, table_num=40, food_quantity=5):
  # clear before test

  (r_browser, c_browser) = tour_TID_039(json_metadata, table_num)

  check_TID_040.run_check(json_metadata, r_browser, 40)

  return (r_browser, c_browser)
