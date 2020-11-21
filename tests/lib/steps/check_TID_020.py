import random

# import item_add_page

from config import *
from time import sleep
from assert_check_point import assertCheckPoint

# from stubs.server.assign_table.helloworld_stub import helloworld_stub
from stubs.server.assign_table.assign_table_by_name import assignTableByName

def run_check(json_metadata, browser, user_name):
  TEST_ERR_MSG='It should send order successfully'

  # helloworld_stub()
  # assign a table to user
  assignTableByName(user_name, random.randrange(2,50,3))


  json_metadata['TID_020'] = 'passed'