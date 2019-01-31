#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 4.py
@time: 2019/1/28 028 10:45
@desc:
'''
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums3 = nums1 + nums2
    nums3.sort()
    if len(nums3) % 2 == 0:
        mid = (nums3[len(nums3)//2] + nums3[len(nums3)//2-1]) / 2
    else:
        mid = nums3[len(nums3)//2]
    return mid

l1 = [1,2]
l2 = [3,4,5]
print(findMedianSortedArrays(l1,l2))