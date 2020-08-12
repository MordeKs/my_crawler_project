# -*- encoding: utf-8 -*-
"""
@File    : create.py
@Time    : 2020/8/12 16:16
@Author  : Morde
@Software: PyCharm
@Description:
"""
from static.detail import Detail
from static.person import Person

detail_kingname = Detail(address='xxx', work='engineer', salary=10000),
kingname = Person(name='kingname', age=23, sex='male', detail=detail_kingname)
detail_xiaoming = Detail(address='yyy', work='pm', salary=0.5),
xiaoming = Person(name='xiaoming', age=65, sex='male', detail=detail_xiaoming)
person_list = [kingname, xiaoming]
for person in person_list:
    detail = person.detail
    salary = detail[0].salary
    print(salary)