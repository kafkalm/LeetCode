#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 39.py
@time: 2019/2/13 013 14:26
@desc:
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    b = []
    def temp(yiyou, t, cand):
        if t in cand:
            b.append(yiyou + [t])
        if t > cand[0]:
            for i in range(len(cand)):
                temp(yiyou + [cand[i]], t - cand[i], cand[i:])

    temp([], target, candidates)
    return b

candidates = [2,3,5]
target = 8
print(combinationSum(candidates,target))

