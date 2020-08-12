# -*- encoding: utf-8 -*-
"""
@File    : person.py
@Time    : 2020/8/12 16:06
@Author  : Morde
@Software: PyCharm
@Description:
"""


class Person(object):
    def __init__(self, name='', age=0, sex='', detail=None):
        self._name = name
        self._age = age
        self._sex = sex
        self._detail = detail

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, new_sex):
        self._sex = new_sex

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, new_detail):
        self._detail = new_detail
