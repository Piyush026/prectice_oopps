from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://www.amazon.in/gp/new-releases/ref=zg_bs_tab/?ref_=nav_cs_newreleases"
uClient = uReq(my_url)
page_url = uClient.read()
uClient.close()
page_soup = soup(page_url, 'html.parser')
containers = page_soup.find_all("div", {"class": "zg_item zg_homeWidgetItem"})
container = containers[0]
# print(container)
first = container.a.find('div', class_="p13n-sc-truncate p13n-sc-line-clamp-4")
first = first.text
print(first)
# <a class="a-link-normal" href="/Indian-Polity-Civil-Services-Examinations/dp/B07Y3CJJCR?_encoding=UTF8&amp;psc=1"><div class="a-section a-spacing-mini"><img alt="Indian Polity - For Civil Services and Other State Examinations | 6th Edition" class="a-dynamic-image p13n-sc-dynamic-image" data-a-dynamic-image='{"https://images-na.ssl-images-amazon.com/images/I/61MrRA4qE0L._AC_UL480_SR372,480_.jpg":[480,372],"https://images-na.ssl-images-amazon.com/images/I/61MrRA4qE0L._AC_UL320_SR248,320_.jpg":[320,248],"https://images-na.ssl-images-amazon.com/images/I/61MrRA4qE0L._AC_UL160_SR124,160_.jpg":[160,124]}' height="160" src="https://images-na.ssl-images-amazon.com/images/I/61MrRA4qE0L._AC_UL160_SR124,160_.jpg" width="124"/></div>
# <div aria-hidden="true" class="p13n-sc-truncate p13n-sc-line-clamp-4" data-rows="4">
#             Indian Polity - For Civil Services and Other State Examinations | 6th Edition
#         </div>
# first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
