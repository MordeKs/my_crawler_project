# -*- encoding: utf-8 -*-
"""
@File    : read_file.py
@Time    : 2020/7/27 10:13
@Author  : Morde
@Software: PyCharm
@Description:
"""
import json
import pprint


dic = {}
with open(r'..\file\text.txt', 'r', encoding='utf-8') as f:
    i = 1
    for line in f.readlines():
        line_list = line.replace('\n', '').split(' ')
        # print(line_list)
        dic[i] = {
            'item':line_list
        }
        i+=1

# print(dic)
pprint.pprint(dic)
# with open(r'..\file\write_text2.txt', 'w', encoding='utf-8') as f:
#     # f.write(str(dic))
#     f.writelines(json.dumps(dic,ensure_ascii=False,indent=4))