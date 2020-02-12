import collections
import json

from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import logging


class MyntraAutomated:

    def __init__(self):
        self.driver = webdriver.Chrome("/home/lovkesh/PycharmProjects/prectice_oops/venv/lib/chromedriver")
        self.driver.set_page_load_timeout(10)
        self.driver.maximize_window()
        self.driver.get("https://www.myntra.com/")
        # ActionChain
        menu = self.driver.find_element_by_xpath("//*[@id='desktop-header-cnt']/div[2]/nav/div/div[1]/div")
        hidden_submenu = self.driver.find_element_by_xpath(
            "//*[@id='desktop-header-cnt']/div[2]/nav/div/div[1]/div/div/div/div/li[3]/ul/li[3]/a")
        ActionChains(self.driver).move_to_element(menu).click(hidden_submenu).perform()

    def HTMLRead(self):
        logging.basicConfig(level=logging.DEBUG, filename='myapp.log', format='%(asctime)s %(levelname)s:%(message)s')
        driver = self.driver
        html = driver.page_source
        page = soup(html, 'html.parser')
        driver.close()
        try:
            containers = page.find_all('li', {"class": "product-base"})
            print(len(containers))
            data = []
            dicts= {}
            for container in containers:
                datanum = {}
                metadata = container.find('div', {'class': 'product-productMetaInfo'})
                brands = metadata.h3.text
                products = metadata.h4.a.text
                price = metadata.find('div', {'class': 'product-price'}).get_text()
                # two ways of data in json form
                free = lambda: collections.defaultdict(free)
                dicts = free()
                dicts[brands][products] = price[4:8]
                # datanum['brand'] = brands
                # datanum['product'] = products
                # datanum['price'] = price[4:8]
                # data.append(datanum)
            # print(data)
                print(json.dumps(dicts))
        except OSError as e:
            logging.error(e, exc_info=True)

        except Exception as exception:
            import traceback
            print(traceback.format_exc(), str(exception))


if __name__ == '__main__':
    my = MyntraAutomated()
    my.HTMLRead()
