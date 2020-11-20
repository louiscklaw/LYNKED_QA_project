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

sys.path.append(LIB_DIR)
sys.path.append(LIB_PO_DIR)
sys.path.append(LANG_DIR)
sys.path.append(LIB_CONFIG_DIR)
sys.path.append(LIB_ASSERT_DIR)

from lib_helloworld import lib_helloworld
from po_helloworld import po_helloworld
from assert_image import assertSameImage

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


def getActualScreenshotPath(test_number):
  return 'reports/UI_test/functional/test_happyflow_1_click_accept_and_continue/{}_sc_iphonex.png'.format(test_number)

def getExpectedScreenshotPath(test_number):
  return 'tests/UI_test/functional/test_happyflow_1_click_accept_and_continue/{}_sc_iphonex.png'.format(test_number)


def check_TID_001(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_001'
  actual_screenshot_path=getActualScreenshotPath('TID_001')
  expected_screenshot_path=getExpectedScreenshotPath('TID_001')

  # URL = 'http://192.168.88.105:8002/'
  # browser.get(URL)
  browser.get(LINE_UP_PAGE)
  sleep(1)

  fl_page = line_up_page.FirstTimeLanding(browser)

  fl_page.checkAcceptAndContinueButtonExist()
  sleep(1)

  fl_page.takeScreenshot(actual_screenshot_path)
  assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  'The device should auto redirect to line up page')
  # fl_page.checkLinkExist()

def check_TID_002(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_002'
  actual_screenshot_path=getActualScreenshotPath('TID_002')
  expected_screenshot_path=getExpectedScreenshotPath('TID_002')

  fl_page = line_up_page.FirstTimeLanding(browser)

  fl_page.tapTAndCText()
  sleep(1)

  fl_page.takeScreenshot(actual_screenshot_path)
  assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  'The device should auto redirect to line up page')

  # back after test
  fl_page.backFromTAndCText()

def check_TID_003(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_003'
  actual_screenshot_path=getActualScreenshotPath('TID_003')
  expected_screenshot_path=getExpectedScreenshotPath('TID_003')

  fl_page = line_up_page.FirstTimeLanding(browser)
  fl_page.tapAcceptAndContinueButton()
  sleep(1)

  fl_page.takeScreenshot(actual_screenshot_path)
  assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  'T&C dialog message should close')

def check_TID_004(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_004'
  actual_screenshot_path=getActualScreenshotPath('TID_004')
  expected_screenshot_path=getExpectedScreenshotPath('TID_004')

  fl_page = line_up_page.FirstTimeLanding(browser)
  # http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?do_lineup

  fl_page.tapCrossButton()

  fl_page.takeScreenshot(actual_screenshot_path)
  assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  'T&C dialog message should close')


def check_TID_005(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_005'
  actual_screenshot_path=getActualScreenshotPath('TID_005')
  expected_screenshot_path=getExpectedScreenshotPath('TID_005')

  fl_page = food_menu.Main(browser)
  fl_page.tapLineUpIcon()

  fl_page.takeScreenshot(actual_screenshot_path)
  assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  'T&C dialog message should close')



def check_TID_006(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_006'
  actual_screenshot_path=getActualScreenshotPath('TID_006')
  expected_screenshot_path=getExpectedScreenshotPath('TID_006')
  TEST_ERR_MSG='User should automatically direct to food menu page with a number display dialog'

  line_up_po = line_up_page.Main(browser)
  dialogue_po= line_up_confirmation_dialogue.Main(browser)

  line_up_po.inputName('this is customer name by louis from script')
  line_up_po.inputNotes('this is customer notse by louis from script')
  line_up_po.changeNumberOfAdult(2)
  line_up_po.changeNumberOfChild(3)

  line_up_po.takeScreenshot(actual_screenshot_path)
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

  line_up_po.submitLineUpTicket()

  dialogue_po.tapOkButtonOnDialogue()

def check_TID_008(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_008'
  actual_screenshot_path=getActualScreenshotPath('TID_008')
  expected_screenshot_path=getExpectedScreenshotPath('TID_008')
  TEST_ERR_MSG='The user info should be updated'

  # before
  fl_page = food_menu.Main(browser)
  line_up_po = line_up_page.Main(browser)
  dialogue_po= line_up_confirmation_dialogue.Main(browser)


  fl_page.takeScreenshot(getActualScreenshotPath('TID_008_01'))
  fl_page.tapTopRightGreenButton()

  # On food menu page, click the number at top right screen

  # Update the name, people, note
  # Update my info
  line_up_po.takeScreenshot(getActualScreenshotPath('TID_008_02'))
  line_up_po.inputName('this is customer name by louis from script updated')
  line_up_po.inputNotes('this is customer notse by louis from script updated')
  line_up_po.changeNumberOfAdult(5)
  line_up_po.changeNumberOfChild(6)

  # Close the info page, check the number at top right screen again
  # Observe
  line_up_po.updateLineUpTicket()
  line_up_po.takeScreenshot(getActualScreenshotPath('TID_008_03'))

  dialogue_po.tapOkButtonOnDialogue()
  line_up_po.takeScreenshot(getActualScreenshotPath('TID_008_04'))

  line_up_po.takeScreenshot(actual_screenshot_path)
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)


def check_TID_009(json_metadata, browser, food_item_idx=1):
  json_metadata['TEST_ID'] = 'TID_009'
  actual_screenshot_path=getActualScreenshotPath('TID_009')
  expected_screenshot_path=getExpectedScreenshotPath('TID_009')
  TEST_ERR_MSG='It should direct to item add page'

  # line_up_po = line_up_page.Main(browser)
  # dialogue_po= line_up_confirmation_dialogue.Main(browser)
  food_menu_po = food_menu.Main(browser)

  food_menu_po.takeScreenshot(getActualScreenshotPath('TID_009_1'))
  food_menu_po.tapFoodItemByIdx(food_item_idx)

  food_menu_po.takeScreenshot(getActualScreenshotPath('TID_009_2'))
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

def check_TID_010(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_010'
  actual_screenshot_path=getActualScreenshotPath('TID_010')
  expected_screenshot_path=getExpectedScreenshotPath('TID_010')
  TEST_ERR_MSG='It should increase the quantity of the food item'

  # line_up_po = line_up_page.Main(browser)
  # dialogue_po= line_up_confirmation_dialogue.Main(browser)
  item_add_page_po = item_add_page.Main(browser)

  item_add_page_po.takeScreenshot(getActualScreenshotPath('TID_010_1'))

  item_add_page_po.addFood()
  item_add_page_po.takeScreenshot(getActualScreenshotPath('TID_010'))
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

def check_TID_011(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_011'
  actual_screenshot_path=getActualScreenshotPath('TID_011')
  expected_screenshot_path=getExpectedScreenshotPath('TID_011')
  TEST_ERR_MSG='It should increase the quantity of the food item'

  # line_up_po = line_up_page.Main(browser)
  # dialogue_po= line_up_confirmation_dialogue.Main(browser)
  item_add_page_po = item_add_page.Main(browser)

  item_add_page_po.takeScreenshot(getActualScreenshotPath('TID_011_1'))
  item_add_page_po.removeFood()

  item_add_page_po.takeScreenshot(getActualScreenshotPath('TID_011'))
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

def check_TID_012(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_012'
  actual_screenshot_path=getActualScreenshotPath('TID_012')
  expected_screenshot_path=getExpectedScreenshotPath('TID_012')
  TEST_ERR_MSG='It should increase the quantity of the food item'

  # line_up_po = line_up_page.Main(browser)
  # dialogue_po= line_up_confirmation_dialogue.Main(browser)
  item_add_page_po = item_add_page.Main(browser)

  item_add_page_po.takeScreenshot(getActualScreenshotPath('TID_012_1'))
  item_add_page_po.tapAddIntoCartButton()

  item_add_page_po.takeScreenshot(getActualScreenshotPath('TID_012'))
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

def check_TID_013(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_013'
  actual_screenshot_path=getActualScreenshotPath('TID_013')
  expected_screenshot_path=getExpectedScreenshotPath('TID_013')
  TEST_ERR_MSG='It should increase the quantity of the food item'

  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)

  food_menu_po.takeScreenshot(getActualScreenshotPath('TID_013_1'))
  food_menu_po.tapCartButton()

  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_013'))

def check_TID_014(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_014'
  actual_screenshot_path=getActualScreenshotPath('TID_014')
  expected_screenshot_path=getExpectedScreenshotPath('TID_014')
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)

  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_014_1'))
  for i in range(1,33):
    cart_page_po.tapAddButton(1)
    sleep(0.05)

  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_014_2'))

  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_014'))
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

def check_TID_015(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_015'
  actual_screenshot_path=getActualScreenshotPath('TID_015')
  expected_screenshot_path=getExpectedScreenshotPath('TID_015')
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)

  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_015_1'))
  for i in range(1,20):
    cart_page_po.tapMinusButton(1)
    sleep(0.05)

  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_015_2'))

  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_015'))
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

def check_TID_016(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_016'
  actual_screenshot_path=getActualScreenshotPath('TID_016')
  expected_screenshot_path=getExpectedScreenshotPath('TID_016')
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)
  item_add_page_po=item_add_page.Main(browser)

  # escape from cart list page from 015
  cart_page_po.tapTopLeftCloseButton()
  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_016_1'))

  # add another food
  food_menu_po.tapFoodItemByIdx(2)
  food_menu_po.takeScreenshot(getActualScreenshotPath('TID_016_2'))

  item_add_page_po.addFood()
  item_add_page_po.takeScreenshot(getActualScreenshotPath('TID_016_3'))

  item_add_page_po.tapAddIntoCartButton()
  item_add_page_po.takeScreenshot(getActualScreenshotPath('TID_016_4'))

  food_menu_po.tapCartButton()
  food_menu_po.takeScreenshot(getActualScreenshotPath('TID_016_5'))

  cart_page_po.tapRemoveButton(1)
  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_016_6'))

  # cart_page_po.takeScreenshot(getActualScreenshotPath('TID_016'))
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

def check_TID_017(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_017'
  actual_screenshot_path=getActualScreenshotPath('TID_017')
  expected_screenshot_path=getExpectedScreenshotPath('TID_017')
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)
  item_add_page_po=item_add_page.Main(browser)
  ERR_MSG='It should send order successfully'

  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_017_1'))
  cart_page_po.tapPlaceOrderButton()
  cart_page_po.takeScreenshot(getActualScreenshotPath('TID_017_2'))


def check_TID_018(json_metadata, browser):
  json_metadata['TEST_ID'] = 'TID_018'
  actual_screenshot_path=getActualScreenshotPath('TID_018')
  expected_screenshot_path=getExpectedScreenshotPath('TID_018')
  ERR_MSG='It should send order successfully'

  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)
  item_add_page_po=item_add_page.Main(browser)
  take_seat_first_dialogue_po=take_seat_first_dialogue.Main(browser)

  take_seat_first_dialogue_po.takeScreenshot(getActualScreenshotPath('TID_018_1'))
  sleep(0.5)

  # tap ok to dismiss dialogue
  take_seat_first_dialogue_po.tapOkButtonOnDialogue()

  take_seat_first_dialogue_po.takeScreenshot(getActualScreenshotPath('TID_018_2'))


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

  check_TID_001(json_metadata, browser)
  check_TID_002(json_metadata, browser)
  check_TID_003(json_metadata, browser)
  check_TID_004(json_metadata, browser)
  check_TID_005(json_metadata, browser)
  check_TID_006(json_metadata, browser)

  # check_TID_007 requires closing browser, skipping
  check_TID_008(json_metadata, browser)
  check_TID_009(json_metadata, browser)
  check_TID_010(json_metadata, browser)
  check_TID_011(json_metadata, browser)
  check_TID_012(json_metadata, browser)
  check_TID_013(json_metadata, browser)
  check_TID_014(json_metadata, browser)
  check_TID_015(json_metadata, browser)
  check_TID_016(json_metadata, browser)
  check_TID_017(json_metadata, browser)
  check_TID_018(json_metadata, browser)


  browser.quit()

  # assertSameImage(EXPECTED_SCREENSHOT, ACTUAL_SCREENSHOT,0.1,  'first time landing test after clicking accept failed')