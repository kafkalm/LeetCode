#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 47.py
@time: 2019/2/14 014 9:54
@desc:
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
#字典序法
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    out = []
    nums.sort()
    flag = 1
    while flag:
        if nums not in out:
            add = []
            for j in nums:
                add.append(j)
            out.append(add)
        for i in range(len(nums)-1,-1,-1):
            if i == 0:
                flag = 0
                break
            if nums[i] > nums[i-1]:
                for k in range(len(nums)-1,i-1,-1):
                    if nums[k] > nums[i-1]:
                        t = nums[k]
                        nums[k] = nums[i-1]
                        nums[i-1] = t
                        break
                if nums not in out:
                    add = []
                    for j in nums:
                        add.append(j)
                    out.append(add)
                num = nums[i:]
                num.reverse()
                nums[i:] = num
                break
    return out