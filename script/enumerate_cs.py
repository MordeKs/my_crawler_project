# -*- encoding: utf-8 -*-
"""
@File    : enumerate_cs.py
@Time    : 2020/8/21 17:47
@Author  : Morde
@Software: PyCharm
@Description:
"""

list1 = ['a','b','c']
list2 = ['d','e','f']

for k, v in enumerate(zip(list1,list2)):
    # print(k,v)
    print(k)
