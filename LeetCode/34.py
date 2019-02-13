#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 34.py
@time: 2019/1/31 031 15:11
@desc:
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。
'''

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    start = 0
    end = len(nums) - 1
    first = -1
    last = -1
    while start<=end:
        mid = (start+end-1)//2
        if nums[mid] == target:
            first = mid
            break
        elif nums[mid] >= nums[start]:
            if nums[mid] < target or nums[start] > target:
                start = mid + 1
            else:
                end = mid - 1
        elif nums[mid] <= nums[end]:
            if nums[mid] > target or nums[end] < target:
                end = mid - 1
            else:
                start = mid + 1
    nums = nums[first+1:]
    start = 0
    end = len(nums) - 1
    while start<=end:
        mid = (start+end)//2
        if nums[mid] == target:
            last = first+mid+1
            break
        elif nums[mid] <= nums[start]:
            if nums[mid] > target or nums[start] < target:
                start = mid + 1
            else:
                end = mid - 1
        elif nums[mid] >= nums[end]:
            if nums[mid] < target or nums[end] > target:
                end = mid - 1
            else:
                start = mid + 1
    out = [first,last]
    return out

nums = [1,3]
target = 2
print(searchRange(nums,target))