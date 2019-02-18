#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 60.py
@time: 2019/2/15 015 11:40
@desc:
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
'''

from operator import itemgetter
def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    nums = list(range(1,n+1))
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
            for i in range(len(nums) - 1, -1, -1):
                if i == 0:
                    flag = 0
                    break
                if nums[i] > nums[i - 1]:
                    for k in range(len(nums) - 1, i - 1, -1):
                        if nums[k] > nums[i - 1]:
                            t = nums[k]
                            nums[k] = nums[i - 1]
                            nums[i - 1] = t
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
        out.sort()
        return out
    out = permute(nums)
    return ''.join([str(x) for x in out[k-1]])

print(getPermutation(3,5))
