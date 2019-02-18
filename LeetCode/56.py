#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 56.py
@time: 2019/2/15 015 9:57
@desc:
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

[[1,3],[2,5],[3,7]]
[[1,6],[2,3],[4,7]]
[[1,4],[5,7]]
'''
from operator import itemgetter
def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if intervals == []:
        return []
    while True:
        intervals.sort(key=itemgetter(0,1))
        count = 0
        for i in range(len(intervals)-1):
            if intervals[i+1][0] <= intervals[i][1] <=intervals[i+1][1] or intervals[i][0] <=intervals[i+1][1] <= intervals[i][1]:
                intervals[i][0] = min(intervals[i][0],intervals[i+1][0])
                intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                intervals[i+1][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i + 1][1])
            else:
                count+=1
                continue
        if count == len(intervals)-1:
            break
        temp_l = list(set([str(i) for i in intervals]))
        intervals = [eval((i)) for i in temp_l]
    return intervals

intervals = [[1,4],[2,3]]
print(merge(intervals))