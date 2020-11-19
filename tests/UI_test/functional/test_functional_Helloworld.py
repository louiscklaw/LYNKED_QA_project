import os,sys
from pprint import pprint

FUNCTIONAL_DIR=os.path.dirname(__file__)
UI_TEST_DIR=os.path.abspath(FUNCTIONAL_DIR+'/..')
TEST_ROOT=os.path.abspath(UI_TEST_DIR+'/..')
TEST_LIB_DIR=os.path.abspath(TEST_ROOT+'/lib')
LIB_PO_DIR=os.path.abspath(TEST_LIB_DIR+'/pages')
LIB_ELE_DIR=os.path.abspath(TEST_LIB_DIR+'/elements')
LIB_CONFIG_DIR=os.path.abspath(TEST_LIB_DIR+'/configs')

sys.path.append(UI_TEST_DIR)
sys.path.append(TEST_ROOT)
sys.path.append(TEST_LIB_DIR)
sys.path.append(LIB_PO_DIR)
sys.path.append(LIB_ELE_DIR)
sys.path.append(LIB_CONFIG_DIR)

from lib_helloworld import lib_helloworld
from po_helloworld import po_helloworld
from ele_helloworld import ele_helloworld
from config_helloworld import config_helloworld

def test_lib_directory():
  pprint(TEST_ROOT)
  # assert a % 2 == 0, "value was odd, should be even"
  assert 'lib_helloworld helloworld'==lib_helloworld()
  assert 'po_helloworld helloworld'==po_helloworld()
  assert 'ele_helloworld helloworld'==ele_helloworld()
  assert 'config_helloworld helloworld'==config_helloworld()

  # pprint(TEST_ROOT)
  # pprint("helloworld_happyflow_1")

def test_functional_Helloworld():
  print("helloworld")
