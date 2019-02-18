#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 57.py
@time: 2019/2/15 015 10:36
@desc:
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
'''

from operator import itemgetter
def insert(intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    intervals.append(newInterval)
    if intervals == []:
        return []
    while True:
        intervals.sort(key=itemgetter(0, 1))
        count = 0
        for i in range(len(intervals) - 1):
            if intervals[i + 1][0] <= intervals[i][1] <= intervals[i + 1][1] or intervals[i][0] <= intervals[i + 1][
                1] <= intervals[i][1]:
                intervals[i][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
            else:
                count += 1
                continue
        if count == len(intervals) - 1:
            break
        temp_l = list(set([str(i) for i in intervals]))
        intervals = [eval((i)) for i in temp_l]
    return intervals