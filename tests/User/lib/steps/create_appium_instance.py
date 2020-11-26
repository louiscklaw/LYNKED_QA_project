from lib.steps.dismiss_jp_translation import dismiss_jp_translation_in_chrome_browser
import unittest
import os
import copy
import sys

import base64

from time import sleep

from appium import webdriver

SCREENCAPTURE_DIR='/home/logic/_workspace/LYNKED_QA_project/tests/User/reports/assets'

def getScreenShot(driver, sc_filename):
  img_data = driver.get_screenshot_as_base64()
  with open(sc_filename, "wb") as fh:
    fh.write(base64.urlsafe_b64decode(img_data))


def create_appium_instance(json_metadata):
  desired_caps = {
      "platformName": "Android",
      "appPackage": "com.android.chrome",
      "appActivity": "com.google.android.apps.chrome.Main"
  }

  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
  sleep(3)
  getScreenShot(driver, '{}/example_com_screen.png'.format(SCREENCAPTURE_DIR))

  context = driver.current_context
  driver.switch_to.context("NATIVE_APP")
  sleep(1)
  driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
  sleep(1)

  driver.find_element_by_id("com.android.chrome:id/negative_button").click()
  sleep(1)

  driver.get('http://www.example.com')

  sleep(15)
  driver.switch_to.context("WEBVIEW_chrome")

  getScreenShot(driver, '{}/after_example_com_screen.png'.format(SCREENCAPTURE_DIR))

  ele_h1 = driver.find_element_by_xpath('/html/body/div/h1')
  sleep(1)

  assert 'Example Domain'==ele_h1.text


  return driver