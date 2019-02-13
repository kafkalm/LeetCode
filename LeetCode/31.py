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
    for i in range(len(nums)-2,-1,-1):
        for j in range(len(nums)-1,i,-1):
            if nums[j] > nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
                nums[i+1:] = sorted(nums[i+1:])
                return nums

    nums.sort()
    return

nums = [1,3,2]
print(nextPermutation(nums))