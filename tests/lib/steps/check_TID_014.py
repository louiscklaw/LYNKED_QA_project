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
  TEST_ERR_MSG='TID_014 failed'
  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)

  assertCheckPoint(browser, 'TID_014_1', TEST_ERR_MSG)
  for i in range(1,33):
    cart_page_po.tapAddButton(1)
    sleep(0.05)

  assertCheckPoint(browser, 'TID_014_2', TEST_ERR_MSG)

  json_metadata['TID_014'] = 'passed'