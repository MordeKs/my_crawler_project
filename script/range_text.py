# -*- encoding: utf-8 -*-
"""
@File    : range_text.py
@Time    : 2020/8/24 11:26
@Author  : Morde
@Software: PyCharm
@Description:
"""
res = ['da', 'df', 'ghh', 'ff']
numb = 0
for i in range(0, 5, 2):
    print(i)
    if i == 0:
        numb = i
        continue
    for j in res[numb:i]:
        print(j)
    numb = i

