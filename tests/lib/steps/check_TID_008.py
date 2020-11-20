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
  TEST_ERR_MSG='The user info should be updated'

  # before
  fl_page = food_menu.Main(browser)
  line_up_po = line_up_page.Main(browser)
  dialogue_po= line_up_confirmation_dialogue.Main(browser)

  assertCheckPoint(browser, 'TID_008_1', TEST_ERR_MSG)
  fl_page.tapTopRightGreenButton()

  # On food menu page, click the number at top right screen

  # Update the name, people, note
  # Update my info
  assertCheckPoint(browser, 'TID_008_2', TEST_ERR_MSG)

  line_up_po.inputName('this is customer name by louis from script updated')
  line_up_po.inputNotes('this is customer notse by louis from script updated')
  line_up_po.changeNumberOfAdult(5)
  line_up_po.changeNumberOfChild(6)

  # Close the info page, check the number at top right screen again
  # Observe
  line_up_po.updateLineUpTicket()
  assertCheckPoint(browser, 'TID_008_3', TEST_ERR_MSG)

  dialogue_po.tapOkButtonOnDialogue()
  assertCheckPoint(browser, 'TID_008_4', TEST_ERR_MSG)

  json_metadata['TID_008'] = 'passed'
