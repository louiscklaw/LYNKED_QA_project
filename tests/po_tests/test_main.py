import os,sys
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep

PO_TEST_DIR=os.path.dirname(__file__)
# /home/logic/_workspace/LYNKED_QA_project/tests
TEST_ROOT=os.path.abspath(PO_TEST_DIR+'/..')
UI_TEST_DIR=os.path.abspath(TEST_ROOT+'/UI_test')
FUNCTIONAL_DIR=os.path.abspath(UI_TEST_DIR+'/functional')

LIB_DIR=os.path.abspath(TEST_ROOT+'/lib')
LIB_PO_DIR=os.path.abspath(LIB_DIR+'/pages')
LIB_ELE_DIR=os.path.abspath(LIB_DIR+'./elements')
LANG_DIR=os.path.abspath(TEST_ROOT+'/lang')
LIB_CONFIG_DIR=os.path.abspath(LIB_DIR+'/configs')
LIB_ASSERT_DIR=os.path.abspath(LIB_DIR+'/asserts')
LIB_STEPS_DIR=os.path.abspath(LIB_DIR+'/steps')

LIB_STUBS_DIR=os.path.abspath(LIB_DIR+'/stubs')
LIB_STUBS_SERVER_DIR=os.path.abspath(LIB_STUBS_DIR+'/server')

sys.path.append(LIB_DIR)
sys.path.append(LIB_PO_DIR)
sys.path.append(LANG_DIR)
sys.path.append(LIB_CONFIG_DIR)
sys.path.append(LIB_ASSERT_DIR)
sys.path.append(LIB_STEPS_DIR)
sys.path.append(LIB_STUBS_DIR)
sys.path.append(PO_TEST_DIR)

import self_test_food_menu
import self_test_line_up_page
import self_test_item_add_page
import self_test_cart_page
import self_test_order_history_page

def test_food_menu_helloworld():
  # self_test_food_menu.try_locate_element()
  # self_test_line_up_page.try_locate_element()
  # self_test_item_add_page.try_locate_element()
  self_test_cart_page.try_locate_element()
  # self_test_order_history_page.try_locate_element()

def test_helloworld():
  print('helloworld')


if __name__=="__main__":
  test_helloworld()