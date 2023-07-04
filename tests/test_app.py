import unittest
from appium import webdriver

class TestApp(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            "platformName": "iOS",
            "platformVersion": "16.4",
            "deviceName": "iPhone SE (3rd generation)",
            "automationName": "XCUITest",
            "app": "/Users/etonealbert/Library/Developer/Xcode/DerivedData/shop-hhyqbkcoodrvcxefchkjkhdpovrr/Build/Products/Debug-iphonesimulator/shop.app",
            "udid": "FD5EB004-5614-4593-9F0B-F67357C13BA8",
            "noReset": True,
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

    #def test_open_close_app(self):
        # App is already launched in the setUp method. You can add any assertions here.
        # After this test method is finished, the app will be closed in the tearDown method.

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
