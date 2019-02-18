#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 59.py
@time: 2019/2/15 015 10:52
@desc:
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

[
 [ 1, 2, 3, 4],
 [12,13,14, 5],
 [11,16,15, 6],
 [10, 9, 8, 7],
'''

def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    out = []
    i = 1
    j = 0
    for k in range(n):
        num = [0] * n
        out.append(num[:])
    while i <= n**2:
        for k in range(j,n-j):
            out[j][k] = i
            i += 1
        for k in range(j+1,n-j):
            out[k][n-j-1] = i
            i += 1
        for k in range(n-j-2,j-1,-1):
            out[n-j-1][k] = i
            i += 1
        for k in range(n-j-2,j,-1):
            out[k][j] = i
            i += 1
        j += 1
    return out

print(generateMatrix(3))
