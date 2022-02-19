"""
作者：RINO
日期: 2022年02月22日
时间: 20:19
"""
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen(
    "https://mofanpy.com/static/scraping/basic-structure.html"
).read().decode('utf-8')
print(html)
import re

res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)  # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])

res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)
