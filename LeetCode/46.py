#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 46.py
@time: 2019/2/14 014 8:54
@desc:
给定一个没有重复数字的序列，返回其所有可能的全排列。

字典排序法
例 [1，2，3，4, 5]
排序完后
第一个输出 [1,2,3,4,5]
从右向左找 第一个非递增的数 5 -> 4 交换
[1,2,3,5,4]
倒排 4
第二个 5 -> 3 找右边最小的比3大的数 交换 （4）
[1,2,4,5,3] 倒排 [5,3]
[1,2,4,3,5] 新序列
第三个 5 -> 3
[1,2,4,5,3]
第四个 5->4
[1,2,5,4,3] 倒排 [4,3]
[1,2,5,3,4]
第五个 4->3
[1,2,5,4,3]
第六个 5->2
[1,3,5,4,2] 倒排 [5,4,2]
[1,3,2,4,5]
----

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
    out.sort()
    return out

#递归法

def permute_2(nums,begin,end):
    out = []
    if begin>=end:
        if nums not in out:
            add = []
            for j in nums:
                add.append(j)
            out.append(add)
    for i in range(begin,end):
        nums[i],nums[begin] = nums[begin],nums[i]
        permute_2(nums,begin+1,end)
        nums[i], nums[begin] = nums[begin], nums[i]
    return out

print(permute([1,2,3]))
# permute_2([1,1,2],0,3)
