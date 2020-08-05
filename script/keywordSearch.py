# -*- encoding: utf-8 -*-
"""
@File    : keywordSearch.py
@Time    : 2020/8/5 9:52
@Author  : Morde
@Software: PyCharm
@Description: 关键词搜索
"""

import re
import time
import requests
from crawler.login import ProQccLogin
import json
import copy
import pymongo
from crawler.spider import QccSpider
from entity.ResultData import ResultData
from logs.Logger import logger


class KeywordSearch():
    def __init__(self,keyword):
        """
        :param keyword:
        """
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
            "Host": "pro.qichacha.com",
        }
        self.cookies = {
            "zg_did": "%7B%22did%22%3A%20%2216ef3d8bbe71c8-0fd241123429f1-7711a3e-100200-16ef3d8bbe829c%22%7D",
            "zg_5d0d048c3009491b8d1244f5b41d003c":
                "%7B%22sid%22%3A%201576049097723%2C%22updated%22%3A%201576049774413%2C%22info%22%3A%201576049097739%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D", }
        self.login_spider = ProQccLogin()
        self.area = '350581'
        self.keyword = keyword
        self.size = 1000
        self.url = 'https://pro.qichacha.com/proapi/common/post'
        self.post_data = {"params":{"searchKey":self.keyword,"searchIndex":"","pageIndex":1,"pageSize":self.size,"sortField":"","isSortAsc":False,"province":"","areaCode":self.area,"industry":"","econkind":"","assetSize":"","revenueLevel":"","netProfit":"","scale":"","startDate":"","status":"","type":"","registCapi":"","insuredCnt":"","flag":"","flagOr":"","tagOr":"","corpType":"","revocationDate":"","cancellationDate":""},"url":"/webapi/saas/expan_cust/multi_sel/list"}

    def search(self):
        headers = copy.copy(self.headers)
        token = self.login_spider.get_token()
        if token:
            headers['pro-access-secret-key'] = token['accessSecretKey']
            headers['pro-access-token'] = token['accessToken']
            headers['pro-client-id'] = token['clientId']
            r = requests.post(
                self.url,
                headers=headers,
                json=self.post_data,
                cookies=self.cookies)
            response_data = r.json()
            return response_data
        else:
            logger.error('获取token失败')


if __name__ == '__main__':
    sorts = {'海洋渔业':['海水养殖','海洋捕捞','渔业服务'],
             '海洋水产品加工业': ['海洋水产品加工业'],
             '海洋油气业': ['海洋石油','海洋天然气','油气开采'],
             '海洋矿业': ['海滨砂矿','海滨土砂石','海底地热'],
             '海洋盐业': ['海水制盐','海盐加工'],
             '海洋船舶工业': ['船舶制造','海洋固定装置','海洋浮动装置'],
             '海洋工程装备制造业': ['海洋设备制造'],
             '海洋化工业': ['海盐化工','海藻化工','海水化工','其他海洋化工'],
             '海洋药物与生物制品业': ['海洋药品','海洋保健品'],
             '海洋工程建筑业': ['海上工程建筑','海底工程建筑','近岸工程建筑'],
             '海洋可再生能源利用业': ['海洋能','海洋风能'],
             '海水利用业': ['海水直接利用','海水淡化','其他海水利用'],
             '海洋交通运输业': ['海洋旅客运输','海洋货物运输','海洋港口','海洋运输辅助'],
             '海洋旅游业': ['海洋旅游业'],
             '海洋信息服务业': ['海洋图书馆','海洋档案馆','海洋出版服务','海洋卫星遥感'],
             '海洋环境监测预报业': ['海洋环境监测','海洋环境预报'],
             '涉海金融服务业': ['涉海直接融资','涉海贷款服务','涉海再保险'],
             '海洋科学研究': ['海洋基础科学研究','海洋工程技术研究'],
             '海洋技术服务业': ['海洋专业技术','海洋工程技术','海洋科技交流'],
             '海洋地质勘查业': ['海洋矿产地质勘查','海洋基础地质勘查'],
             '海洋生态环境保护业': ['海洋自然环境','海洋环境治理','海洋生态修复'],
             '海洋教育': ['海洋中等教育','海洋高等教育','海洋职业教育'],
             '海洋管理': ['海洋综合管理','海洋经济管理','海洋公共安全管理'],
             '海洋社团与国际组织': ['海洋社会团体','海洋行业团体'],
             '海洋农、林业': ['海洋农业','海洋林业','海洋农林服务'],
             '涉海设备制造': ['为海洋生产与管理活动提供仪器,装置,设备及配件等的制造活动','涉海设备制造'],
             '海洋仪器制造': ['海洋专用仪器'],
             '涉海产品再加工': ['海洋水产品深加工','海洋化工产品'],
             '海洋产品批发': ['海洋产品批发'],
             '海洋产品零售': ['海洋产品零售'],
             '涉海服务业': ['海洋餐饮','滨海公共运输','海洋金融'],
             '涉海建筑与安装业': ['涉海建筑与安装','涉海建筑工程安装'],
             '涉海原材料制造': ['水产养殖饲料','海洋工艺品','海洋环保材料'],
             '海洋新材料制造': ['海洋防护材料','海洋特殊材料制造'],
             }
    # sorts = {'海洋渔业': ['海水养殖','海洋捕捞']}
    for key,value in sorts.items():
        for item in value:
            print(item)
            spider = KeywordSearch(item)
            result = spider.search()
            result_list = result.get('resultList',[])
            client = pymongo.MongoClient(
                'mongodb://credit:credit@10.2.1.56:27017,10.2.1.79:27017,10.2.13.251:27018/credit?replicaSet=pszxdb')
            db = client['credit']['SS_Marineindustry']
            try:
                for i in result_list:
                    i['sort'] = key
                    i['keyword'] = item
                    i['process'] = 1
                    print(i)
                    db.update_one({'sort':i['sort'],'keyword':i['keyword'],'name':i['name']},{'$set':i},upsert=True)
            finally:
                client.close()