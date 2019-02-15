#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 48.py
@time: 2019/2/14 014 10:13
@desc:
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    matrix[:] = [list(x[::-1]) for x in zip(*matrix)]
    print(matrix)

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate(matrix)
print(matrix)