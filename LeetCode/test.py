#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: test.py
@time: 2019/1/28 028 13:18
@desc:
'''
l = [1,1,2,2,3,3,4,4,5,5,7,7,9,9,8]
d = {}
for i in range(len(set(l))):
    num = l[i]
    if d.get(num) == None:
        d[num] = 1
        l.pop(i)
    if num in l:
        continue
    else:
        print(num)


