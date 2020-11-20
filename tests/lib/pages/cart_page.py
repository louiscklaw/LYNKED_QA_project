import os,sys
from pprint import pprint

FIRST_ADD_BUTTON='//*[@id="plus"]'
# add button 1
# /html/body/main/div[8]/div[2]/div[2]/div[2]/div[3]/button[2]

# add button 2
# /html/body/main/div[8]/div[2]/div[3]/div[2]/div[3]/button[2]

# del button 1
# /html/body/main/div[8]/div[2]/div[2]/div[2]/div[3]/button[1]

# remove 削除
# /html/body/main/div[8]/div[2]/div[2]/div[3]/button
# /html/body/main/div[8]/div[2]/div[3]/div[3]/button

TOP_LEFT_CLOSE_BUTTON_XPATH='//*[@id="close"]'
PLACE_ORDER_BUTTON_XPATH='/html/body/main/div[8]/div[3]/div'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
      self.driver = driver

    def takeScreenshot(self, sc_filename):
      self.driver.save_screenshot(sc_filename)

    def tapButton(self, xpath):
      ele_button = self.driver.find_element_by_xpath(xpath)
      ele_button.click()

    def getFoodItemXpathFromIdx(self, item_idx):
      return '/html/body/main/div[8]/div[2]/div[{}]'.format(item_idx+1)

    def getAddButtonXpath(self, item_idx):
      return '{}/div[2]/div[3]/button[2]'.format(self.getFoodItemXpathFromIdx(item_idx))

    def getMinusButtonXpath(self, item_idx):
      return '{}/div[2]/div[3]/button[1]'.format(self.getFoodItemXpathFromIdx(item_idx))

    def getRemoveButtonXpath(self, item_idx):
      return '{}/div[3]/button'.format(self.getFoodItemXpathFromIdx(item_idx))

    def tapAddButton(self, item_idx):
      self.tapButton(self.getAddButtonXpath(item_idx))

    def tapMinusButton(self, item_idx):
      self.tapButton(self.getMinusButtonXpath(item_idx))

    def tapRemoveButton(self, item_idx):
      self.tapButton((self.getRemoveButtonXpath(item_idx)))

    def tapTopLeftCloseButton(self):
      self.tapButton(TOP_LEFT_CLOSE_BUTTON_XPATH)

    def tapPlaceOrderButton(self):
      self.tapButton(PLACE_ORDER_BUTTON_XPATH)

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
