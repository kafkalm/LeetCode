#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 8.py
@time: 2019/1/29 029 10:04
@desc:
'''
def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    if str != '':
        s = str.lstrip(' ')
        num = ['0','1','2','3','4','5','6','7','8','9']
        out = ''
        if s[0] == '-':
            out = '-'
            for i in range(1,len(s)):
                if s[i] in num:
                    out = out + s[i]
                else:
                    break
        elif s[0] in num:
            out = s[0]
            for i in range(1,len(s)):
                if s[i] in num:
                    out = out + s[i]
                else:
                    break
        elif s[0] == '+':
            out = ''
            for i in range(1,len(s)):
                if s[i] in num:
                    out = out + s[i]
                else:
                    break
        else:
            out = 0
        if out != '-' and out != '':
            if int(out) < (-2)**31:
                return -2147483648
            elif int(out) > (2 ** 31 -1):
                return 2147483647
        else:
            return 0
        return int(out)
    else:
        return 0
print(myAtoi('+'))