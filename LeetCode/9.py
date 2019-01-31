#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 9.py
@time: 2019/1/29 029 10:19
@desc:
'''
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    s = str(x)
    return s == s[::-1]

print(isPalindrome(0))