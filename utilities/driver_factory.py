from appium import webdriver

def create_driver():
    desired_cap = {
        "platformName": "iOS",
        "platformVersion": "16.4",
        "deviceName": "iPhone SE (3rd generation)",
        "automationName": "XCUITest",
        "app": "/path/to/your/.app or .ipa file",
        "udid": "your device udid",
        "noReset": True,
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    return driver

