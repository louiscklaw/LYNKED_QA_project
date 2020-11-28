from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# mobile_emulation = {
#     "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
#     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

def setupRemoteChrome():
  caps = webdriver.DesiredCapabilities.CHROME.copy()

  selenium_url = 'http://{}:4444/wd/hub'.format('localhost')

  mobile_emulation = { "deviceName": "Nexus 5" }
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
  chrome_options.add_experimental_option('w3c', False)

  # chrome_options.add_argument("--headless")

  caps=chrome_options.to_capabilities()
  caps['acceptInsecureCerts'] = True


  browser = webdriver.Remote(
    command_executor=selenium_url,
    desired_capabilities = chrome_options.to_capabilities()
  )

  return browser

  # selenium_url = 'http://{}:4444/wd/hub'.format(SELENIUM_HUB_HOST)
  # chrome_options = webdriver.ChromeOptions()
  # mobile_emulation = { "deviceName": "Nexus 5" }
  # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

  # browser = webdriver.Remote(
  #   command_executor=selenium_url,
  #   desired_capabilities = chrome_options.to_capabilities()
  # )
  # pass