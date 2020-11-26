import random
from pprint import pprint

import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page

import table_assigned_dialogue

# import item_add_page

from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

# from stubs.server.assign_table.helloworld_stub import helloworld_stub
from stubs.server.assign_table.assign_table_by_name import assignTableByName

def run_check(json_metadata, browser):
  TEST_ERR_MSG = 'ERROR RUNNING TID_020'
  # check cart page

  assertCheckPoint(browser, 'TID_020_1', 'TEST_ERR_MSG')

  json_metadata['TID_020'] = 'passed'
