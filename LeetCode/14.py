#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 14.py
@time: 2019/1/29 029 15:22
@desc:最长前缀
'''

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    flag = 0
    out = ''
    if len(strs) > 0 :
        for k in range(len(strs[0])):
            prefix = strs[0][:k+1]
            for i in strs:
                if i[:len(prefix)] != prefix:
                    flag = 1
                    break
            if flag:
                break
            out = prefix
    return out

strs = []
print(longestCommonPrefix(strs))