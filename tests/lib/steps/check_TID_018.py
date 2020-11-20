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
  TEST_ERR_MSG='It should send order successfully'

  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)
  item_add_page_po=item_add_page.Main(browser)
  take_seat_first_dialogue_po=take_seat_first_dialogue.Main(browser)

  assertCheckPoint(browser, 'TID_018_1', TEST_ERR_MSG)
  sleep(0.5)

  # tap ok to dismiss dialogue
  take_seat_first_dialogue_po.tapOkButtonOnDialogue()

  assertCheckPoint(browser, 'TID_018_2', TEST_ERR_MSG)

  json_metadata['TID_018'] = 'passed'