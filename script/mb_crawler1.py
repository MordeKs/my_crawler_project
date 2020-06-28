# -*- encoding: utf-8 -*-
"""
@File    : mb_crawler1.py
@Time    : 2020/6/26 11:30
@Author  : MordeKs
@Email   : Gjay@163.com
@Software: PyCharm
@Description:
"""
import requests
from bs4 import BeautifulSoup

url = "https://www.qu.la/"
header = {
    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "cookie":"__cfduid=d714794d236005e14652cfca73660e46e1566460333; Hm_lvt_5ee23c2731c7127c7ad800272fdd85ba=1566460334; bcolor=; font=; size=; fontcolor=; width=; bookid=22299%2C101104%2C66788; chapterid=8219183%2C5281139%2C3587301; chaptername=%25u7B2C%25u4E00%25u767E%25u4E03%25u5341%25u516D%25u7AE0%2520%25u521D%25u6597%25u9F99%25u95E8%2C%25u7B2C%25u4E00%25u7AE0%2520%25u90A3%25u662F%25u4EC0%25u4E48%253F%2C%25u7B2C26%25u7AE0%2520%25u695A%25u884C%25u4E91%25u7684%25u8BA1%25u5212; fontFamily=null; fontColor=null; fontSize=null; bg=null; UM_distinctid=172ea49f5036b-00e33223e7e59e-4353761-100200-172ea49f504100; CNZZDATA1278951146=1589434158-1593067298-%7C1593067298; Hm_lvt_2e4e957b2529bd3b60d576d577d639bf=1593068615; bookid=22299; booklist=%257B%2522BookId%2522%253A22299%252C%2522ChapterId%2522%253A4201061%252C%2522ChapterName%2522%253A%2522%25u7B2C%25u4E00%25u7AE0%2520%25u6211%25u53EB%25u65B9%25u9A8F%25u7709%2522%257D; ASP.NET_SessionId=jvfrkyzkkyxj51fwkdt5cz5m; Hm_lpvt_2e4e957b2529bd3b60d576d577d639bf=1593068633",
}
basic_wb_text = requests.get(url,headers = header)
wb_text = basic_wb_text.text.encode('ISO-8859-1').decode()
soup = BeautifulSoup(wb_text,'lxml')
title = soup.select("div.layout.layout-col2 > div > dl > dt > a")
for t in title:
    print(t.get_text())