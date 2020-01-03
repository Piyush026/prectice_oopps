from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("/home/lovkesh/PycharmProjects/prectice_oops/venv/lib/chromedriver")
driver.get("https://www.guru99.com/selenium-python.html")
driver.implicitly_wait(10)

menu = driver.find_element_by_xpath("/html/body/div[2]/section[2]/div/div/div[2]/div/nav/ul/li[3]/div/span[1]/span")

hidden_submenu = driver.find_element_by_xpath("/html/body/div[2]/section[2]/div/div/div[2]/div/nav/ul/li["
                                              "3]/ul/li/div/div[2]/ul/li[4]/a/span/span")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
driver.back()
