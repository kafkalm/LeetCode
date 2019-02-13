#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 40.py
@time: 2019/2/13 013 14:50
@desc:
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''


def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    b = []

    def temp(yiyou, t, cand):
        if cand == []:
            return None
        if t in cand:
            if yiyou+[t] not in b:
                b.append(yiyou + [t])
        if t > cand[0]:
            for i in range(len(cand)):
                temp(yiyou + [cand[i]], t - cand[i], cand[i+1:])

    temp([], target, candidates)
    return b

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates,target))