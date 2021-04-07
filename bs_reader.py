import requests
import re
from bs4 import BeautifulSoup

def cup_of_soup(rss, addr):
    result = rss.get(addr)
    print("Connection state:", result.status_code)

    bs = BeautifulSoup(result.text, 'lxml')

    return bs



webaddr = "https://mofanpy.com/static/scraping/list.html"
webaddr_regex = "https://mofanpy.com/static/scraping/table.html"

s = requests.sessions.Session()
s.keep_alive = False



soup = cup_of_soup(s, webaddr)

# 所有anchor的href attributes
#     若是內容是anchor.string
for anchor in soup.find_all('a'):
    print(anchor['href'])

for obj_month in soup.find_all(class_='month'):
    print(obj_month.string)

# 找出january底下的list item
for jandate in soup.find(class_= 'jan').find_all('li'):
    print(jandate.string)



soup = cup_of_soup(s, webaddr_regex)

# 找出格式為jpg的所有圖片
jpgs = soup.find_all('img', src=re.compile('.*\.jpg'))
print(jpgs)

# 找出隸屬於https://morvan下的超連結
hrefs = soup.find_all(href=re.compile('/.*'))
for i in hrefs:
    print(i['href'])