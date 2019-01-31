#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 26.py
@time: 2019/1/30 030 16:01
@desc:给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
'''

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    idx = 0
    for i in range(len(nums)):
        a = nums.pop(idx)
        if a not in nums:
            nums.insert(idx,a)
            idx = idx +1
    print(nums)
    return len(nums)

def removeDuplicates(nums):
    """
    双指针法
    因为只需修改前几个元素 不需要删除
    :param nums:
    :return:
    """
    numLen = len(nums)
    if numLen == 0:
        return 0

    i = 0
    for j in range(1, numLen):
        if nums[j] != nums[i]:
            i = i + 1
            nums[i] = nums[j]
    print(nums)
    return i + 1

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))