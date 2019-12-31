from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # cls.driver = webdriver.Chrome(executable_path=r"../venv/lib/chromedriver")
        cls.driver = webdriver.Chrome("/home/lovkesh/PycharmProjects/prectice_oops/venv/lib/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.fullscreen_window()

    def testSearchOne(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Amazon")
        self.driver.find_element_by_name("btnK").click()

    def testSearchTwo(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("myntra")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/lovkesh/PycharmProjects/prectice_oops/report"))
