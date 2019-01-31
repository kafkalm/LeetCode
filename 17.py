#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 17.py
@time: 2019/1/29 029 16:19
@desc:递归找出字母组合
'''

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dic = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
           '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
    out_l = []
    for i in digits:
        out_l.append(dic[i])
    out = []
    if len(digits)>1:
        out = get_it(out_l[0],out_l[1:])
    elif len(digits)==1:
        out = out_l[0]
    return out

def get_it(l1,l2):
    if l2 == []:
        return l1
    out = [a+b for a in l1 for b in l2[0]]
    l2.pop(0)
    return get_it(out,l2)
print(letterCombinations(''))