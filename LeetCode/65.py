#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 65.py
@time: 2019/2/15 015 15:10
@desc:
验证给定的字符串是否为数字。

例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

没意思

'''

def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    try:
        float(s)
        return True
    except:
        return False