import os,sys
from pprint import pprint

TEST_DIR=os.path.dirname(__file__)
FUNCTIONAL_DIR=os.path.abspath(TEST_DIR+'/..')
UI_TEST_DIR=os.path.abspath(FUNCTIONAL_DIR+'/..')
TEST_ROOT=os.path.abspath(UI_TEST_DIR+'/..')
TEST_LIB_DIR=os.path.abspath(TEST_ROOT+'/lib')
LIB_PO_DIR=os.path.abspath(TEST_LIB_DIR+'/page_object')

sys.path.append(TEST_DIR)
sys.path.append(UI_TEST_DIR)
sys.path.append(TEST_ROOT)
sys.path.append(TEST_LIB_DIR)
sys.path.append(LIB_PO_DIR)

from lib_helloworld import lib_helloworld
from po_helloworld import po_helloworld

def test_happyflow_1():
  print('helloworld')
