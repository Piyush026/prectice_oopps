from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://books.google.co.in/books?hl=en&lr=&id=AK44DwAAQBAJ&oi=fnd&pg=PA2&dq=Google+IT+Automation+with" \
         "+Python+Professional+Certificate&ots=I6B9mbBqiX&sig=XqcNpo1fB57YcT54BOk_WgPjlBQ&redir_esc=y#v=onepage&q&f" \
         "=false "
uClient = uReq(my_url)
page_url = uClient.read()
# uClient.close()
page_soup = soup(page_url, 'html.parser')
# prettyHTML = page_soup.prettify()
# print(prettyHTML)
containers = page_soup.find("div", {"id":"viewport"})
prettyHTML= containers.prettify()
print(prettyHTML)