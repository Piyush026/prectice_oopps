import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/home/lovkesh/PycharmProjects/prectice_oops/venv/lib/chromedriver")

driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("gmail")
driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div[1]/div[3]/center/input[1]").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()

