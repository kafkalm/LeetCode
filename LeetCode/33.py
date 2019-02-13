#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 33.py
@time: 2019/1/31 031 14:33
@desc:
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

时间复杂度 O(log n)  (二分法)

因此一次遍历不可行 时间复杂度为 O(n)
'''

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[start]:
            if target > nums[mid] or target < nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        elif nums[mid] <= nums[end]:
            if target < nums[mid] or target > nums[end]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums,target))
