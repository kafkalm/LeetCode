#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 55.py
@time: 2019/2/15 015 9:36
@desc:
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。
示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

贪心算法
'''


def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    idx = 0
    for i in range(len(nums)):
        #能到达的最远下标
        cur = i + nums[i]
        if cur > idx:
            #跳跃到最远处
            idx = cur
        if idx >= len(nums) - 1:
            return True
        if idx <= i:
            #代表nums[i] = 0 达到不了
            return False

nums = [0]
print(canJump(nums))
