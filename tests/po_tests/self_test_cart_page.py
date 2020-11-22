import os,sys
from pprint import pprint
from selenium import webdriver

from config import *
from time import sleep

from po_helloworld import *

import line_up_page
import item_add_page
import cart_page

def setupLocalChrome():
  caps = webdriver.DesiredCapabilities.CHROME.copy()

  chrome_options = webdriver.ChromeOptions()

  mobile_emulation = { "deviceName": "Nexus 5" }
  chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
  # chrome_options.add_argument("--headless")

  caps=chrome_options.to_capabilities()
  caps['acceptInsecureCerts'] = True

  browser = webdriver.Chrome('drivers/chrome/86/chromedriver', desired_capabilities=caps)
  return browser


def po_helloworld_test():
  po_helloworld()

def try_locate_remove_button(po):
  po.tapRemoveButton(2)


def try_locate_element():
  browser = setupLocalChrome()
  food_item_list=['http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/5f6205657f11c030c1ddf6f2',
  'http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/5f6205d47f11c030c1ddf8d6']

  # dismiss initial accept and continue
  browser.get(food_item_list[0])

  item_add_po=item_add_page.FirstTimeLanding(browser)
  item_add_po.tapAcceptAndContinueButton()

  for u in food_item_list:
    browser.get(u)

    item_add_po=item_add_page.Main(browser)

    # item_add_po.tapCrossButton()
    item_add_po.addFood()
    item_add_po.addFood()
    item_add_po.addFood()
    item_add_po.tapAddIntoCartButton()

  item_add_po.tapBottomCartPageButton()

  cart_page_po=cart_page.Main(browser)
  for i in range(1,2+1):
    cart_page_po.tapAddButton(i)
    cart_page_po.tapAddButton(i)
    cart_page_po.tapAddButton(i)
    cart_page_po.tapAddButton(i)
    cart_page_po.tapAddButton(i)
    cart_page_po.tapMinusButton(i)
    cart_page_po.tapMinusButton(i)

  try_locate_remove_button(cart_page_po)

  sleep(3)

  browser.quit()
