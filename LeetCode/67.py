#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 67.py
@time: 2019/2/15 015 15:34
@desc:
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if len(a)>=len(b):
        b='0'*abs(len(a)-len(b))+b
    else:
        a = '0' * abs(len(a) - len(b)) + a
    a = [int(x) for x in list(a)]
    b = [int(x) for x in list(b)]
    res = [0]*(max(len(a),len(b))+1)
    flag = 0
    for i in range(-1,-len(a)-1,-1):
        res[i] = (a[i] + b[i] + flag) % 2
        if a[i] + b[i] + flag >= 2:
            flag = 1
        else:
            flag = 0
    res[0] = flag
    out = ''.join([str(x) for x in res])
    out = out.lstrip('0')
    if out != '':
        return out
    else:
        return '0'

a="1111"
b="1111"
print(addBinary(a,b))