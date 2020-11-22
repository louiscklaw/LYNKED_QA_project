import os,sys
from pprint import pprint
from selenium import webdriver

from config import *
from time import sleep

from po_helloworld import *
import food_menu


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

def locate_cart_button(browser):
  fm_po = food_menu.Main(browser)
  fm_po.tapCartButton()

def locate_fooditem(browser):
  fm_po = food_menu.Main(browser)
  fm_po.getFoodItemFromList(1)
  fm_po.getFoodItemFromList(2)
  fm_po.getFoodItemFromList(3)
  fm_po.getFoodItemFromList(4)
  fm_po.getFoodItemFromList(5)

def try_locate_element():
  browser = setupLocalChrome()
  browser.get('http://menymeny.com/food/%E3%82%84%E3%81%8D%E3%81%A8%E3%82%8A/')

  fm_po=food_menu.FirstTimeLanding(browser)
  fm_po.tapAcceptAndContinueButton()

  locate_fooditem(browser)
  locate_cart_button(browser)

  browser.quit()

  print('food_menu_helloworld_test')
