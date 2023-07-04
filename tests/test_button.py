from appium import webdriver

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

def test_button_click():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    
    try:
        el = driver.find_element_by_accessibility_id('buttonAccessibilityId')
        el.click()

        # add an assertion here based on what should happen when the button is clicked
        # e.g., check the app's state or verify the UI
    finally:
        driver.quit()

