
import os,sys
from pprint import pprint

ADD_BUTTON_XPATH='/html/body/main/div[8]/div[2]/div[5]/div[1]/button[2]'
DEL_BUTTON_XPATH='/html/body/main/div[8]/div[2]/div[5]/div[1]/button[1]'

NUM_OF_ITEM_XPATH='/html/body/main/div[8]/div[2]/div[5]/div[1]/div'
UNIT_PRICE_XPATH='/html/body/main/div[8]/div[2]/div[4]/div'
FOOD_NAME_XPATH='/html/body/main/div[8]/div[2]/div[2]/div'
FOOD_INFO_XPATH='/html/body/main/div[8]/div[2]/div[3]/div'

TOP_LEFT_CLOSE_BUTTON_XPATH='//*[@id="close"]'
ADD_INTO_CART_BUTTON_XPATH='//*[@id="addtocart"]'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
      self.driver = driver

    def tapButton(self, xpath):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.click()

    def addFood(self):
      self.tapButton(ADD_BUTTON_XPATH)

    def removeFood(self):
      self.tapButton(DEL_BUTTON_XPATH)

    def tapAddIntoCartButton(self):
      self.tapButton(ADD_INTO_CART_BUTTON_XPATH)

    def takeScreenshot(self, sc_filename):
        self.driver.save_screenshot(sc_filename)

class Main(BasePage):
  def getLineUpIcon(self):
    return self.driver.find_element_by_xpath(LINE_UP_ICON_XPATH)

  def tapLineUpIcon(self):
    self.getLineUpIcon().click()

  def tapTopRightGreenButton(self):
    self.tapButton(TOP_RIGHT_GREEN_BUTTON)


class FirstTimeLanding(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()
    def helloworld(self):
      print('helloworld')
