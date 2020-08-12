# -*- encoding: utf-8 -*-
"""
@File    : detail.py
@Time    : 2020/8/12 16:14
@Author  : Morde
@Software: PyCharm
@Description:
"""


class Detail(object):
    def __init__(self, address='', work='', salary=0):
        self._address = address
        self._work = work
        self._salary = salary

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        self._address = new_address

    @property
    def work(self):
        return self._work

    @work.setter
    def work(self, new_work):
        self._work = new_work

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
