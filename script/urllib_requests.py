# -*- encoding: utf-8 -*-
"""
@File    : urllib_requests.py
@Time    : 2020/8/17 10:55
@Author  : Morde
@Software: PyCharm
@Description:urllib和requests的区别
"""
import urllib
import requests
import base64
import json


class Request:
    def __init__(self):
        self.url = 'http://www.xbiquge.la/images/logo.png'
        self.heders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }

    def urllib_(self):
        html = urllib.request.urlopen(self.url)
        return html.read()

    def requests_(self):
        html = requests.get(self.url)
        return base64.b64encode(html.content)


if __name__ == '__main__':
    r = Request()
    print(type(r.requests_()))
    print(r.urllib_())