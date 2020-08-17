# -*- encoding: utf-8 -*-
"""
@File    : use_yield.py
@Time    : 2020/8/13 11:57
@Author  : Morde
@Software: PyCharm
@Description:
"""

import redis
import datetime
import pymongo


client = redis.Redis()
handler = pymongo.MongoClient().data_list.num_yield

CHINESE_NUM_DICT = {
    '一': '1',
    '二': '2',
    '三': '3',
    '四': '4',
    '五': '5',
    '六': '6',
    '七': '7',
    '八': '8',
    '九': '9'
}


def get_data():
    while True:
        data = client.lpop('datalist')
        if not data:
            break
        yield data.decode()


def remove_sensitive_data(datas):
    for data in datas:
        if data == '敏感信息':
            continue
        yield data


def tranfer_chinese_num(datas):
    for data in datas:
        try:
            num = int(data)
        except ValueError:
            num = ''.join(CHINESE_NUM_DICT[x] for x in data)
        yield num


def save_data(number_list):
    for number in number_list:
        data = {'num': number, 'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        handler.insert_one(data)


raw_data = []
safe_data = remove_sensitive_data(raw_data)
number_list = tranfer_chinese_num(safe_data)
save_data(number_list)
