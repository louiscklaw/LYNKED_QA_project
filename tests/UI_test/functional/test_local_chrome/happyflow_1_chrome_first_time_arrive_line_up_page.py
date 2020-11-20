import os,sys
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
LIB_STEPS_DIR=os.path.abspath(LIB_DIR+'/steps')

sys.path.append(LIB_DIR)
sys.path.append(LIB_PO_DIR)
sys.path.append(LANG_DIR)
sys.path.append(LIB_CONFIG_DIR)
sys.path.append(LIB_ASSERT_DIR)
sys.path.append(LIB_STEPS_DIR)

from lib_helloworld import lib_helloworld
from po_helloworld import po_helloworld
from assert_image import assertSameImage
from assert_check_point import assertCheckPoint
# from steps_helloworld import steps_helloworld

from steps import *

# import POs
import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page
import take_seat_first_dialogue


from jp import *

SELENIUM_HUB_HOST='localhost'
LINE_UP_PAGE='http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?do_lineup'

# ACTUAL_SCREENSHOT='reports/UI_test/functional/test_happyflow_1_click_accept_and_continue/sc_to_check.png'
# TID_001_EXPECTED_SCREENSHOT='tests/UI_test/functional/test_happyflow_1_click_accept_and_continue/expected_result/TID_001_expected_sc_iphonex.png'
# TID_002_EXPECTED_SCREENSHOT='tests/UI_test/functional/test_happyflow_1_click_accept_and_continue/expected_result/TID_002_expected_sc_iphonex.png'


def takeScreenshot(driver, sc_filename):
    driver.save_screenshot(sc_filename)

def getActualScreenshotPath(test_number):
  return 'reports/UI_test/functional/test_happyflow_1_click_accept_and_continue/{}_sc.png'.format(test_number)

def getExpectedScreenshotPath(test_number):
  return 'tests/UI_test/functional/test_happyflow_1_click_accept_and_continue/expect/{}_sc.png'.format(test_number)

def test_happyflow_1_chrome_first_time_arrive_line_up_page(json_metadata):
  caps = webdriver.DesiredCapabilities.CHROME.copy()

  chrome_options = webdriver.ChromeOptions()

  mobile_emulation = { "deviceName": "Nexus 5" }
  chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
  # chrome_options.add_argument("--headless")

  caps=chrome_options.to_capabilities()
  caps['acceptInsecureCerts'] = True

  browser = webdriver.Chrome('drivers/chrome/86/chromedriver', desired_capabilities=caps)


  # selenium_url = 'http://{}:4444/wd/hub'.format(SELENIUM_HUB_HOST)

  # chrome_options = webdriver.ChromeOptions()
  # mobile_emulation = { "deviceName": "Nexus 5" }
  # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

  # browser = webdriver.Remote(
  #   command_executor=selenium_url,
  #   desired_capabilities = chrome_options.to_capabilities()
  # )

  check_TID_001.run_check(json_metadata, browser)
  check_TID_002.run_check(json_metadata, browser)
  check_TID_003.run_check(json_metadata, browser)
  check_TID_004.run_check(json_metadata, browser)
  check_TID_005.run_check(json_metadata, browser)
  check_TID_006.run_check(json_metadata, browser)
  check_TID_007.run_check(json_metadata, browser)
  check_TID_008.run_check(json_metadata, browser)
  check_TID_009.run_check(json_metadata, browser)
  check_TID_010.run_check(json_metadata, browser)
  check_TID_011.run_check(json_metadata, browser)
  check_TID_012.run_check(json_metadata, browser)
  check_TID_013.run_check(json_metadata, browser)
  check_TID_014.run_check(json_metadata, browser)
  check_TID_015.run_check(json_metadata, browser)
  check_TID_016.run_check(json_metadata, browser)
  check_TID_017.run_check(json_metadata, browser)
  check_TID_018.run_check(json_metadata, browser)


  browser.quit()

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')