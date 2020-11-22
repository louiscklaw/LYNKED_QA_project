import os,sys
from pprint import pprint
from selenium import webdriver

from config import *
from time import sleep

from po_helloworld import *

import line_up_page
import item_add_page

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


def try_add_food(po):
  po.addFood()
  po.addFood()
  po.addFood()
  po.addFood()
  po.addFood()
  po.addFood()
  po.addFood()

def try_remove_food(po):
  po.removeFood()
  po.removeFood()
  po.removeFood()

def try_close(po):
  po.tapCrossButton()

def try_locate_element():
  browser = setupLocalChrome()
  browser.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/5f6205657f11c030c1ddf6f2')

  item_add_po=item_add_page.FirstTimeLanding(browser)
  item_add_po.tapAcceptAndContinueButton()

  item_add_po=item_add_page.Main(browser)
  try_add_food(item_add_po)
  try_remove_food(item_add_po)

  try_close(item_add_po)

  browser.quit()
