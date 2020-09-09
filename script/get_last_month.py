# -*- encoding: utf-8 -*-
"""
@File    : get_last_month.py
@Time    : 2020/9/3 11:39
@Author  : Morde
@Software: PyCharm
@Description: 获取上个月，上几个月的日期
"""

import datetime

def getTheMonth(n):
    date = datetime.datetime.today()
    month = date.month
    year = date.year
    day = date.day
    for i in range(n):
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
    return datetime.date(year, month, day).strftime('%Y-%m-%d')

def getdate(beforeOfDay):
    today = datetime.datetime.now()
    # 计算偏移量
    offset = datetime.timedelta(days=-beforeOfDay)
    # 获取想要的日期的时间
    re_date = (today + offset).strftime('%Y-%m-%d')
    return re_date
# 测试
# print(getTheMonth(3))
print(getdate(90))