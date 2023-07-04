class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        el = self.driver.find_element_by_id('username_input_field')  # replace with actual id
        el.clear()
        el.send_keys(username)

    def enter_password(self, password):
        el = self.driver.find_element_by_id('password_input_field')  # replace with actual id
        el.clear()
        el.send_keys(password)

    def click_login_button(self):
        el = self.driver.find_element_by_id('login_button')  # replace with actual id
        el.click()
