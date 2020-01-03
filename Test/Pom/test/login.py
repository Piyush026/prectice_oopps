import unittest
from selenium import webdriver
import HtmlTestRunner
import time
from Test.Pom.pages.LoginPage import LoginPage
from Test.Pom.pages.homePage import HomePage


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("/home/lovkesh/PycharmProjects/prectice_oops/venv/lib/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.fullscreen_window()

    def testSearchOne(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login = LoginPage(driver)
        login.enterUsername("Admin")
        login.enterPassword("admin123")
        login.clickLogin()

        time.sleep(2)
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

    def testSearchTwo(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login = LoginPage(driver)
        login.enterUsername("Admin1")
        login.enterPassword("admin123")
        login.clickLogin()
        message = driver.find_element_by_xpath("//*[@id='spanMessage']").text
        self.assertEqual(message, " Invalid credentials")

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/lovkesh/PycharmProjects/prectice_oops/report"))
