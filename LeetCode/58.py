#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 58.py
@time: 2019/2/15 015 10:43
@desc:
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
'''

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    l = s.split(' ')
    for i in range(len(l)-1,-1,-1):
        if len(l[i]) != 0:
            return len(l[i])
    return 0

s = "Hello World"
print(lengthOfLastWord(s))
