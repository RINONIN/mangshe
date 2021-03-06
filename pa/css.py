"""
作者：RINO
日期: 2022年02月22日
时间: 20:35
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/list.html").read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features='lxml')

# use class to narrow search
month = soup.find_all('li', {"class": "month"})
for m in month:
    print(m.get_text())

jan = soup.find('ul', {"class": 'jan'})
d_jan = jan.find_all('li')  # use jan as a parent
for d in d_jan:
    print(d.get_text())