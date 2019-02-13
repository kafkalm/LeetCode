#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 41.py
@time: 2019/2/13 013 15:04
@desc:
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
'''

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    if len(nums) == 0 or nums[-1] <=0 :
        return 1
    else:
        for i in range(1,nums[-1]+2):
            if i not in nums:
                return i

nums = [3,4,-1,1]
print(firstMissingPositive(nums))