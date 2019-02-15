#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 42.py
@time: 2019/2/13 013 15:21
@desc:
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

先找到最高的柱子
分别从左向右 从右向左往最高的柱子遍历
记录遇到的最高的柱子
遇到矮的柱子 area += 最高柱子 - 矮的柱子

'''


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    mid = 1
    left = 0
    right = 2
    total_area = 0
    while mid < len(height) - 1:
        if height[mid] < height[left] and height[mid] < height[right]:
            while left-1 > -1 and height[left-1] > height[left]:
                left = left - 1
            while right+1 < len(height) and height[right+1] > height[right]:
                right = right + 1
            area = min(height[left],height[right]) * (right-left+1)
            for i in height[left:right+1]:
                if i > min(height[left],height[right]):
                    area -= min(height[left],height[right])
                else:
                    area -= i
            total_area += area
        mid += 1
        left = mid - 1
        right = mid + 1
    return total_area

def trap(height):
    if len(height)>2:
        max_idx = height.index(max(height))
        h = 0
        v = 0
        for i in range(max_idx):
            if height[i] > h:
                h = height[i]
            else:
                v = v + h - height[i]
        h = 0
        for i in range(len(height)-1,max_idx,-1):
            if height[i] > h:
                h = height[i]
            else:
                v = v + h - height[i]
        return v
    else:
        return 0
height = [5,2,1,2,1,5]
print(trap(height))

