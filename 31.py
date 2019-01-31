#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 31.py
@time: 2019/1/30 030 17:55
@desc:
'''

def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        if nums[len(nums)-1-i] > nums[len(nums)-2-i]