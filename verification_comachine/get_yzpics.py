# -*- encoding: utf-8 -*-
"""
@File    : get_yzpics.py
@Time    : 2020/8/19 9:42
@Author  : Morde
@Software: PyCharm
@Description: 获取验证码图片
"""
import requests

headers = {
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'chkphone=acWxNpxhQpDiAchhNuSnEqyiQuDIO0O0O; __jsluid_s=2e6195fa455fd19a7c3d5e12ffab614d; ci_session=0213631ff40f3a4230225822a735a277ea2e390e',
    'Host': 'user.ichunqiu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://user.ichunqiu.com/login/verify_image?d=1523697519026',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
}
yzmheaders={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'JSESSIONID=F1C67D1AFDFD7C9FA70DF36CEA781F01; Hm_lvt_d59e2ad63d3a37c53453b996cb7f8d4e=1597801206; _gscbrs_15322769=1; _gscu_15322769=97801214cqrgn254; SESSION=0e767346-57a6-4ebc-9a3c-e8fca06fdd6e; _gscs_15322769=t978212560xm1qc26|pv:1; Hm_lpvt_d59e2ad63d3a37c53453b996cb7f8d4e=1597821257',
'Host': 'zxgk.court.gov.cn',
'Referer': 'http://zxgk.court.gov.cn/zhzxgk/',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
}

# url = "https://user.ichunqiu.com/login/verify_image?d=1523697519026"
url = "http://zxgk.court.gov.cn/zhzxgk/captcha.do?captchaId=a27733c0ee7c4deb8afd082c0197e217&random=0.03244159977401362"
for i in range(0, 20):
    with open("./zxgk_yzm/{}.png".format(i), "wb") as f:
        print("{} pic downloading...".format(i))
        f.write(requests.get(url, headers=yzmheaders).content)
