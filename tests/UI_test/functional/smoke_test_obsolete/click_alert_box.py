import os,sys
from pprint import pprint

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from time import sleep

TEST_DIR=os.path.dirname(__file__)
FUNCTIONAL_DIR=os.path.abspath(TEST_DIR+'/..')
UI_TEST_DIR=os.path.abspath(FUNCTIONAL_DIR+'/..')
TEST_ROOT=os.path.abspath(UI_TEST_DIR+'/..')
LIB_DIR=os.path.abspath(TEST_ROOT+'/lib')
LIB_PO_DIR=os.path.abspath(LIB_DIR+'/pages')
LIB_ELE_DIR=os.path.abspath(LIB_DIR+'./elements')
LANG_DIR=os.path.abspath(TEST_ROOT+'/lang')
LIB_CONFIG_DIR=os.path.abspath(LIB_DIR+'/configs')
LIB_ASSERT_DIR=os.path.abspath(LIB_DIR+'/asserts')

sys.path.append(LIB_DIR)
sys.path.append(LIB_PO_DIR)
sys.path.append(LANG_DIR)
sys.path.append(LIB_CONFIG_DIR)
sys.path.append(LIB_ASSERT_DIR)

from lib_helloworld import lib_helloworld
from po_helloworld import po_helloworld
from assert_image import assertSameImage
import line_up_page
import food_menu
import line_up_confirmation_dialogue


OK_BUTTON_PATH='/html/body/div[2]/input'

def test_click_alert_box():
  # Optional argument, if not specified will search path.
  browser = webdriver.Chrome('drivers/chrome/86/chromedriver')
  browser.get('http://127.0.0.1:8002/test_click_alertbox.html')

  time.sleep(1)   # Let the user actually see something!

  lineup_dialogue_po = line_up_confirmation_dialogue.Main(browser)
  lineup_dialogue_po.tapOkButtonOnDialogue()

  time.sleep(5)
  browser.quit()
