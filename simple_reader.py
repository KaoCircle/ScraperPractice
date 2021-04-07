# open url with requests.session
# scrap simple website information with regex

# regular expression module
import re
import requests

webaddr = "https://mofanpy.com/static/scraping/basic-structure.html"

# 開啟一次session來讀取網頁
s = requests.sessions.Session()
s.keep_alive = False
result = s.get(webaddr)

# success code = 200
print("Connection state:", result.status_code)

# r""內填入所需的正規表示
# 找出title
# findall: return all matched string (list)
ptn = r"<title>(.*)</title>"
t = re.findall(ptn, result.text)
print("Title:")
print(t[0])

# 找出paragraph
# DOTALL模式下符號.也包含換行字元
ptn = r"<p>(.*)</p>"
p = re.findall(ptn, result.text, re.DOTALL)
print("\nParagraph:")
print(p[0])

# 找出所有超連結
# *list 以seperater分別印出list item
ptn = r'href="(.*)"'
a = re.findall(ptn, result.text)
print("\nHyperlinks:")
print(*a, sep = "\n")