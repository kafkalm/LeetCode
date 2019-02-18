#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 73.py
@time: 2019/2/15 015 17:49
@desc:
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
'''


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    # i 行 j 列
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                for k in range(len(matrix[0])):
                    if matrix[i][k] != 0:
                        matrix[i][k] = 'a'
                for k in range(len(matrix)):
                    if matrix[k][j] != 0:
                        matrix[k][j] = 'a'
    for i in range(len(matrix)):
        matrix[i] = [str(x) for x in matrix[i]]
        matrix[i] = ''.join(matrix[i])
        matrix[i] = matrix[i].replace('a','0')
        matrix[i] = list([int(x) for x in matrix[i]])
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] == 'a':
    #             matrix[i][j] = 0
    print(matrix)

matrix = [[-1],[2],[3]]
setZeroes(matrix)
