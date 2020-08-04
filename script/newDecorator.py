# -*- encoding: utf-8 -*-
"""
@File    : newDecorator.py
@Time    : 2020/7/27 14:14
@Author  : Morde
@Software: PyCharm
@Description:
"""

def a_ne_decorator(func):

    def welcome():
        return 'welcome'+func()
    return welcome()

@a_ne_decorator
def a_person():
    return '李雷'

a_person()
