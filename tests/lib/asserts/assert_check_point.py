from assert_image import assertSameImage
from time import sleep

def takeScreenshot(driver, sc_filename):
    driver.save_screenshot(sc_filename)

def getActualScreenshotPath(test_number):
  return 'tests/UI_test/functional/smoke_test/actual/{}_sc.png'.format(test_number)

def getExpectedScreenshotPath(test_number):
  return 'tests/UI_test/functional/smoke_test/expected/{}_sc.png'.format(test_number)

def assertCheckPoint(driver ,check_point_name, error_message, fail_threshold=0.05, sleep_s=0.5, make_asserts=True):
  sleep(sleep_s)
  actual_screenshot_path=getActualScreenshotPath(check_point_name)
  expected_screenshot_path=getExpectedScreenshotPath(check_point_name)

  takeScreenshot(driver, actual_screenshot_path)

  if make_asserts:
    assertSameImage(expected_screenshot_path, actual_screenshot_path,fail_threshold,  error_message)
