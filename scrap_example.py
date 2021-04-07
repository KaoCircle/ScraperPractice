import re
import random
import requests
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen


headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

base_url = 'https://baike.baidu.com'
his = ['/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711']

s = requests.sessions.Session()
s.keep_alive = False


for i in range(20):
    url_content = s.get(base_url+his[-1], headers=headers)
    url_content.encoding = 'utf-8'
    bs = BeautifulSoup(url_content.text, 'lxml')

    print(bs.title.string, " url:", his[-1])

    urls = bs.find_all(target="_blank", href=re.compile('^/item/(%.{2})+$'))

    if len(urls)>0:
        his.append(random.sample(urls, 1)[0]['href'])
    else:
        his.pop()

    time.sleep(3)