"""
作者：RINO
日期: 2022年02月22日
时间: 20:48
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/table.html").read().decode('utf-8')
# print(html)

soup = BeautifulSoup(html, features='lxml')

# img_links = soup.find_all("img", {"src": re.compile('.*?\\.jpg')})
# for link in img_links:
#     print(link['src'])

course_links = soup.find_all('a', {'href': re.compile('/tutorials*')})
for link in course_links:
    print(link['href'])
