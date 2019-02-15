#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 53.py
@time: 2019/2/14 014 11:14
@desc:
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


'''

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    else:
        sum = nums[0]
        temp = 0
        for i in nums:
            if temp+i > i:
                temp = temp+i
            else:
                temp = i
            sum = max(temp,sum)
    return sum
    # sum = 0
    # max_sub_sum = nums[0]
    # for i in nums:
    #     sum = sum + i
    #     max_sub_sum = max(sum,max_sub_sum)
    #     # if sum > max_sub_sum:
    #     #     max_sub_sum = sum
    #     if sum < 0:
    #         sum = 0
    # return max_sub_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))