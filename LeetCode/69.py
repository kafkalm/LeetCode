#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 69.py
@time: 2019/2/15 015 16:42
@desc:
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
'''


#慢
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        for i in range(x//2,0,-1):
            if i**2 <= x <= (i+1)**2:
                return i

#二分法
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        left = 1
        right = x - 1
        while left <= right:
            mid = (left + right)//2
            if mid ** 2 <= x <(mid+1)**2:
                return mid
            elif mid**2 < x:
                left = mid+1
            elif mid**2 > x:
                right = mid -1

print(mySqrt())