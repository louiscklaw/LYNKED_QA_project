import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *
from setupLocalChrome import *

from steps import *
from pages.config import *
from jp import *

def test_TID_helloworld(json_metadata):

  browser = setupLocalChrome()
  browser.get("http://127.0.0.1:8003/test_div_array.html")
  eles = browser.find_elements_by_xpath('//*[@id="orders"]/div[not(@hide)]/div[2]/div')
  for ele in eles:
    pprint(ele.text)
  assert False, len(eles)

  return browser
