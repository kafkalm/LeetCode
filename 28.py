#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 28.py
@time: 2019/1/30 030 16:19
@desc:实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
'''

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # XD
    return haystack.find(needle)

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == '':
        return 0
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(strStr('hello','ll'))