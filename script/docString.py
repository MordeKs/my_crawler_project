# -*- encoding: utf-8 -*-
"""
@File    : docString.py
@Time    : 2020/7/17 16:43
@Author  : Morde
@Software: PyCharm
@Description:
"""

def println(strr):
    """
    我是打印'hello world'
    :return:
    """
    # strr_list = strr.split(' ')
    # strr_list[0] = strr_list[0].capitalize()
    # strr_list[1] = strr_list[1].capitalize()
    # after_strr = ' '.join(strr_list)
    # strr = strr.title()
    # strr = strr[::-1]
    # strr = ''.join(reversed(strr))
    # after_strr = '我要打印%s' %strr
    # after_strr = '我要打印{}'.format(strr)
    # after_strr = '我要打印{0}'.format(strr)
    after_strr = strr.encode('GBK').decode('UTF-8','ignore')
    print(after_strr)# 打印

"""
 (1)s="info：xiaoZhang 33 shandong"，
 用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
 (2) a = "你好 中国 "，去除多余空格只留一个空格。
"""
a = "info：xiaoZhang 33 shandong"
b = "你好 中国 "
# println('hello world')


import re
# content = re.findall(r'(.*)：(.*?).(\d{2}).(.*)',a)
# content = b.strip()
# content = re.findall(r'(.*).',b)
# print(content)
import json
# a,b=b,a
# print(a,b)
# print(json.dumps(b))# ,ensure_ascii=False

# word1 = 'cba'
# word2 = 'dfg'
# word3 = word1+word2
# word3 = sorted(word3)
# print(''.join(word3))

# import datetime
# def datetime_operate(n:int)->str:
#     now = datetime.datetime.now()
#     _new_day = now+datetime.timedelta(days=n)
#     new_day = _new_day.strftime('%Y.%m.%d')
#     return new_day
#
# print(datetime_operate(3))

# def outside(args):
#     def inside():
#         print('内层函数执行',args)
#     return inside()
#
# outside('哈哈')


# def strappend(num):
#     s='first'
#     for i in range(num):
#         s+=str(i)
#         yield s
# print([i for i in strappend(2)])

# print(list(range(2,101,2)))

import json

# dic = {'a':123, 'b':"456", 'c':"liming"}
# # 转换成json格式
# dic_ = str(dic).replace("'", "\"")
# # print(dic_)
# # # loads：json对象转换成字典对象
# dic_str = json.loads(dic_)
# print(dic_str)

# with open('../file/text.txt','r') as f:
#     count = 0
#     for word in f.read():
#         if word.isupper():
#             count+=1
#     print(count)
# import pymongo
# client = pymongo.MongoClient(host='127.0.0.1',port='27017')
# db = client['db']
# table = db['table']
#
# table.find()
# import redis
# r = redis.Redis(host='lacalhost',port=6379,db=0)
# r.get('name')
# r.mget('name1','name2')
# r.set('name','zhangsan')
# r.mset({'name1':'lisi','name2':'wangwu'})
# r.setrange('name',1,'z')
# import pymysql
# conn = pymysql.connect(host='127.0.0.1',port=3306)

# aa = [('a',1),('b',2),('c',3),('d',4)]
# a_1 = list(map(lambda x:x[0],aa))
# print(a_1)
# import abc
# class mytest:
#     __mataclass__ = abc.ABCMeta
#     def __init__(self,args):
#         """
#
#         :param args:
#         """
#         self.args = args
#
#     @abc.abstractmethod
#     def speaking(self,input):
#         return

def first_upper(astring):
    assert isinstance(astring, str) and len(astring) > 0
    result = astring[0].upper()
    assert isinstance(result, str) and len(result) == 1
    assert result == result.upper()
    return result

# print(first_upper('L'))
# print('mordeKs'.capitalize())

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
class E(C, A):
    pass
class F(D, E):
    pass
class M:
    pass
class N(M):
    pass
class P(E, A):
    pass
class X:
    pass
class Q(P,N,X):
    pass
class G(Q, F):
    pass
class H(G, F):
    pass

# print(G.mro())
# print(A().__dir__())

def longdef(a,b,*args,**kwargs):
    return kwargs

print(longdef(1,2,'22','33','44',c=33,d=44))