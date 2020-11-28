import os,sys
from pprint import pprint
from selenium import webdriver

from config import *
from time import sleep

from po_helloworld import *

import line_up_page
import order_history_page

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

def try_input_name(po):
  po.inputName('hello input name')

def try_input_notes(po):
  po.inputNotes('hello input notes')

def try_numberOfAdult(po):
  po.changeNumberOfAdult(2)

def try_numberOfChild(po):
  po.changeNumberOfChild(2)


def try_locate_element():
  browser = setupLocalChrome()
  browser.get('http://127.0.0.1:8080/order_history_page_with_order.html')

  # line_up_po=line_up_page.FirstTimeLanding(browser)
  # line_up_po.tapAcceptAndContinueButton()

  order_history_with_order_po=order_history_page.WithOrder(browser)
  order_history_with_order_po.updateNumberOfPeople(2)
  order_history_with_order_po.updateNumberOfPeople(3)
  order_history_with_order_po.updateNumberOfPeople(4)
  # try_input_name(order_history_po)
  # try_input_notes(order_history_po)
  # try_numberOfAdult(order_history_po)
  # try_numberOfChild(order_history_po)

  # browser.quit()

  pprint('hello order history')