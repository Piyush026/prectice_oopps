class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_textbox_name = "Submit"
        self.invalid_xpath = "//*[@id='spanMessage']"

    def enterUsername(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_name(self.login_textbox_name).click()

    def invalidAccess(self):
        msg = self.driver.find_element_by_xpath(self.invalid_xpath).text
        return msg
