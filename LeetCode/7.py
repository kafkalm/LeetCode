#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 7.py
@time: 2019/1/29 029 9:49
@desc:
'''
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x != 0 and x != -0 :
        s = str(x)
        out = s[::-1]
        out = out.lstrip('0')
        if out[len(out) - 1] == '-':
            out = out[:-1]
            out = '-' + out
        out = int(out)
        if out < (-2) ** 31 or out > (2 ** 31 - 1):
            return 0
        return out
    else:
        return 0

print(reverse(1534236469))