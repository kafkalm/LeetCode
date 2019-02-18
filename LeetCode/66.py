#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 66.py
@time: 2019/2/15 015 15:12
@desc:
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
'''

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if digits == []:
        return digits
    digits[-1] += 1
    for i in range(len(digits)-1,0,-1):
        if digits[i] < 10:
            break
        else:
            digits[i] -= 10
            digits[i-1] += 1
    if digits[0] >= 10:
        digits[0] -= 10
        digits.insert(0,1)
    return digits

digits = [4,2,1,9]
print(plusOne(digits))