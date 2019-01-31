#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 11.py
@time: 2019/1/29 029 14:15
@desc:水桶最大面积
'''
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    start = 0
    end = len(height)
    max_area = min(height[start],height[end-1])*(end-start-1)
    for i in range(len(height)-1):
        if height[start]>height[end-1]:
            end = end - 1
            if min(height[start],height[end-1])*(end-start-1) > max_area:
                max_area = min(height[start],height[end-1])*(end-start-1)
        else:
            start = start + 1
            if min(height[start],height[end-1])*(end-start-1) > max_area:
                max_area = min(height[start],height[end-1])*(end-start-1)
    return max_area,start,end

l = [1,8,6,2,5,4,8,3,7]
# l = [1,2]
# l = [1,2,4,3]
# l = [2,3,4,5,18,17,6]
print(maxArea(l))