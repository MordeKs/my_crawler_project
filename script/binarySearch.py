# -*- encoding: utf-8 -*-
"""
@File    : binarySearch.py
@Time    : 2020/7/27 11:26
@Author  : Morde
@Software: PyCharm
@Description: 二分查找
"""

def bin_search(array,val):
    low = 0 # 列表最小索引
    high = len(array)-1 # 列表最大索引
    while low<=high:
        mid = (low+high)//2 # 列表中间数下标
        if array[mid] == val:
            return mid
        elif array[mid]>val: # 如果val在中间数的左边，则移动high下标,反之,low下标上移
            high-=1
        else:
            low+=1
    return

item_list = sorted(['小明','小华','Mike','Morde'])
print(item_list)
ret = bin_search(item_list,'小明')
print(ret)
print(item_list.index('小明'))

