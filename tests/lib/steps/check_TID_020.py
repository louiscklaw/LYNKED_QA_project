import random
from pprint import pprint

import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page
import take_seat_first_dialogue
import table_assigned_dialogue

# import item_add_page

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

# from stubs.server.assign_table.helloworld_stub import helloworld_stub
from stubs.server.assign_table.assign_table_by_name import assignTableByName

def run_check(json_metadata, browser):
  # check cart page

  assertCheckPoint(browser, 'TID_020_1', TEST_ERR_MSG)

  cart_page_po = cart_page.Main(browser)


  assertCheckPoint(browser, 'TID_020_2', TEST_ERR_MSG)

  json_metadata['TID_020'] = 'passed'
