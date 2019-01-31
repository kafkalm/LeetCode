#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 20.py
@time: 2019/1/29 029 17:33
@desc:判断括号合法（使用栈）
'''
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    dic_left = {'{':'}','[':']','(':')'}
    dic_right = {'}':'{',']':'[',')':'('}
    stack = []
    if len(s) % 2 != 0:
        return False
    else:
        for i in s:
            if i in dic_left:
                stack.append(i)
            else:
                if stack != []:
                    if dic_right[i] != stack.pop(-1):
                        return False
                else:
                    return False
    if stack == []:
        return True
    else:
        return False

s = '(('
print(isValid(s))