#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 22.py
@time: 2019/1/30 030 9:49
@desc:生成括号 回溯算法
'''

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    stack = []
    gent(n,'',stack)
    return stack


def gent(n,s,l,left=0,right=0):
    if len(s) == 2*n:
        l.append(s)
        return True
    if left < n:
        gent(n,s+'(',l,left+1,right)
    if right < left:
        gent(n,s+')',l,left,right+1)

print(generateParenthesis(3))

