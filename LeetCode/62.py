#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 62.py
@time: 2019/2/15 015 13:12
@desc:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

必定要走 m - 1 + n - 1 步
从 m - 1 + n - 1中挑出m-1步的走法即可
C((m+n-2),(m-1))
'''

from functools import reduce
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    def jc(n):
        if n == 0:
            return 1
        return reduce(lambda x, y: x * y, range(1, n + 1))
    return jc(m+n-2)//(jc(m-1)*jc(n-1))

print(uniquePaths(3,4))