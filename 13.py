#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 13.py
@time: 2019/1/29 029 15:14
@desc:罗马字符转数字
'''

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500,
           'CM':900, 'M':1000}
    out = []
    i = 0
    while i < len(s):
        if i < len(s) - 1 and dic[s[i]] < dic[s[i+1]]:
            out.append(dic[s[i:i+2]])
            i = i + 2
        else:
            out.append(dic[s[i]])
            i = i + 1
    output = sum(out)
    return output

print(romanToInt("MCMXCIV"))