#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 70.py
@time: 2019/2/15 015 16:58
@desc:
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

f(3) = f(2) + f(1)
f(4) = f(3) + f(2)
典型动态规划
'''


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    map = [-1]*n
    def dp(x):
        if map[x-1] != -1:
            return map[x-1]
        if x == 1:
            map[x-1] = 1
        elif x == 2:
            map[x-1] = 2
        else:
            map[x-1] = dp(x-1) + dp(x-2)
        return map[x-1]
    dp(n)
    return map[n-1]

print(climbStairs(4))