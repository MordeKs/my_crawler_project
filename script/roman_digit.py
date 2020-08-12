# -*- encoding: utf-8 -*-
"""
@File    : roman_digit.py
@Time    : 2020/8/12 16:40
@Author  : Morde
@Software: PyCharm
@Description: 罗马数字和阿拉伯数字相互转换
"""

romanNumeralMap = (('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1))


def to_roman(n):
    result = ''
    for numeral,integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result


def from_roman(s):
    result = 0
    index = 0
    for numeral,integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


# print(to_roman(1234))
print(from_roman('MMCMLXXII'))