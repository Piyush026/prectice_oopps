from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.amazon.in/gp/new-releases/ref=zg_bs_tab/?ref_=nav_cs_newreleases"
uClient = uReq(my_url)
page_url = uClient.read()
uClient.close()
page_soup = soup(page_url, 'html.parser')
containers = page_soup.find_all("div", {"class": "zg_item zg_homeWidgetItem"})
print(len(containers))

new_dict = []
stars = []
writers = []
names = []
for container in containers:
    if container.find('div', {'class': "a-icon-row a-spacing-none"}) is not None:
        name = container.find('div', {"class": "p13n-sc-truncate p13n-sc-line-clamp-4"})
        names.append(name.text.replace('\n', '').strip())
        writer = container.find('span', {'class': 'a-size-small a-color-base'})
        # print(writer)
        writers.append(writer)
        star = container.find('span', {"a-icon-alt"})
        stars.append(star.text)
    else:
        name = container.find('div', {"class": "p13n-sc-truncate p13n-sc-line-clamp-5"})
        names.append(name.text.replace('\n', '').strip())
        writer = container.find('span', {'class': 'a-size-small a-color-base'})
        writers.append(writer.text)

print(names)
print(writers)
# print([i for i,x in enumerate(writers) if x == "Sadhguru"])
# print(stars)

