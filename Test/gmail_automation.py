from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re


class GmailAutomation:
    def __init__(self):
        # using chrome
        self.driver = webdriver.Chrome("/home/lovkesh/PycharmProjects/prectice_oops/venv/lib/chromedriver")
        self.driver.set_page_load_timeout(10)

        # open gmail
        self.driver.get(
            "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service"
            "=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    def gmailRead(self):

        # login gmail
        gmailId = self.driver.find_element_by_name("identifier")
        gmailId.send_keys("piyush.17mca3047@abes.ac.in")

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span").click()
        self.driver.implicitly_wait(4)
        gmailPassword = self.driver.find_element_by_name("password")
        gmailPassword.send_keys("Piyush@890")
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span").click()
        # open first mail

        firstMail = self.driver.find_element_by_xpath("//*[@id=':22']")
        firstMail.click()

        textData = self.driver.find_element_by_xpath(
            "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div["
            "1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div["
            "1]/div[2]/div[3]/div[3]/div/div[1]/div["
            "1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr/td")
        text = textData.text
        print(text)

        time.sleep(4)
        self.driver.quit()


if __name__ == '__main__':
    GA = GmailAutomation()
    GA.gmailRead()


