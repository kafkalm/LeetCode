#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 35.py
@time: 2019/2/13 013 9:50
@desc:
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
'''

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    try:
        return nums.index(target)
    except:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start+end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return start

nums = []
target = 7
print(searchInsert(nums,target))


