import random
from pprint import pprint

import lib.pages.please_take_seat_first_dialogue as please_take_seat_first_dialogue
import lib.pages.line_up_page as line_up_page
import lib.pages.food_menu as food_menu
import lib.pages.line_up_confirmation_dialogue as line_up_confirmation_dialogue
import lib.pages.item_add_page as item_add_page
import lib.pages.cart_page as cart_page


from lib.config import *
from time import sleep
from lib.asserts.assert_check_point import assertCheckPoint

from stubs.server.assign_table.assign_table_by_name import assignTableByName

import restaurant_manage.admin_page

def run_check(json_metadata, browser):
  TEST_ERR_MSG='test failed at TID_029'

  assertCheckPoint(browser, 'TID_029_1', TEST_ERR_MSG)

  admin_page_po = restaurant_manage.admin_page.Main(browser)
  admin_page_po.tapSiteNavigator()

  assertCheckPoint(browser, 'TID_029_2', TEST_ERR_MSG)

  admin_page_with_site_nav_po = restaurant_manage.admin_page.SiteNavigatorPopup(browser)
  # lineups
  admin_page_with_site_nav_po.tapSeatReservationManagmentButton()

  assertCheckPoint(browser, 'TID_029_3', TEST_ERR_MSG)

  json_metadata['TID_029'] = 'passed'
