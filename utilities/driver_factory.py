from appium import webdriver

def create_driver():
    desired_cap = {
      "platformName": "iOS",
      "platformVersion": "14.4",  # replace with your iOS device version
      "deviceName": "iPhone 11",  # replace with your device name
      "automationName": "XCUITest",
      "app": "/path/to/your/.app or .ipa file",  # replace with path to .app or .ipa file
      "udid": "your device udid",  # replace with your device UDID
      "noReset": True,  # prevents the app from getting reset before the test
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    return driver
