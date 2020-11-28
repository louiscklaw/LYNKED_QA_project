import os,sys
from pprint import pprint
from selenium import webdriver

from config import *
from time import sleep

from po_helloworld import *

import line_up_page

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
  browser.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/?do_lineup')

  line_up_po=line_up_page.FirstTimeLanding(browser)
  line_up_po.tapAcceptAndContinueButton()

  line_up_po=line_up_page.Main(browser)
  try_input_name(line_up_po)
  try_input_notes(line_up_po)
  try_numberOfAdult(line_up_po)
  try_numberOfChild(line_up_po)

  browser.quit()
