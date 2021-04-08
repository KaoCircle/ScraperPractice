import re
import random
import requests
from bs4 import BeautifulSoup

print('\n\n') #just for console look

headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
turl = 'http://pythonscraping.com/pages/cookies/welcome.php'
purl = 'http://pythonscraping.com/pages/cookies/profile.php'
uid = {'username':'people', 'password': 'password'}

s = requests.Session()

# logging in
target_return = s.post(turl, data = uid)
print(target_return.cookies.get_dict())

profile_return = s.get(profile_url)
print(profile_return.text)