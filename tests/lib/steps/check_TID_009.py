import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page
import take_seat_first_dialogue

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

def run_check(json_metadata, browser):
  TEST_ERR_MSG='It should direct to item add page'

  # line_up_po = line_up_page.Main(browser)
  # dialogue_po= line_up_confirmation_dialogue.Main(browser)
  food_menu_po = food_menu.Main(browser)

  assertCheckPoint(browser, 'TID_009_1', TEST_ERR_MSG)
  food_menu_po.tapFoodItemByIdx(1)

  assertCheckPoint(browser, 'TID_009_2', TEST_ERR_MSG)
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

  json_metadata['TID_009'] = 'passed'
