# -*- encoding: utf-8 -*-
"""
@File    : first_crawler.py
@Time    : 2020/6/25 14:28
@Author  : MordeKs
@Email   : Gjay@163.com
@Software: PyCharm
@Description:
"""

from bs4 import BeautifulSoup
import requests

url = "https://www.qu.la/"
r = requests.get(url)
r = r.text.encode('ISO-8859-1').decode()
# print(r)
soup = BeautifulSoup(r,'lxml')
title = soup.select('body > div.container > div > div > div > div > dl > dt > a')
for i in title:
    print(i.get_text())
# print(soup)
