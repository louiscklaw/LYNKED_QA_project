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
  TEST_ERR_MSG='User should automatically direct to food menu page with a number display dialog'

  line_up_po = line_up_page.Main(browser)
  dialogue_po= line_up_confirmation_dialogue.Main(browser)

  line_up_po.inputName('this is customer name by louis from script')
  line_up_po.inputNotes('this is customer notse by louis from script')
  line_up_po.changeNumberOfAdult(2)
  line_up_po.changeNumberOfChild(3)

  assertCheckPoint(browser, 'TID_005_1', TEST_ERR_MSG)
  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

  line_up_po.submitLineUpTicket()

  dialogue_po.tapOkButtonOnDialogue()
  json_metadata['TID_006'] = 'passed'
