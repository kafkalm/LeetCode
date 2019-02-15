#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 54.py
@time: 2019/2/14 014 13:27
@desc:
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16],
  [17,18,19,20]
]
输出: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

[
  [1, 2, 3],
  [5, 6, 7],
  [8, 9, 10],
  [11,12,13],
  [14,15,16]
'''

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    out=[]
    if matrix == []:
        return []
    def print_4(l,m,n):
        if m == 1:
            out.extend(l[0])
            return None
        if n == 1:
            for i in range(m):
                out.extend(l[i])
            return None
        else:
            out.extend(l.pop(0))
            for i in range(len(l)-1):
                out.append(l[i].pop(-1))
            a = l.pop(-1)
            a.reverse()
            out.extend(a)
            for i in range(len(l)-1,-1,-1):
                out.append(l[i].pop(0))
                if l[i] == []:
                    l.pop(i)
            if l == []:
                return None
        print_4(l,len(l),len(l[0]))
    print_4(matrix,len(matrix),len(matrix[0]))
    return out

matrix =[[1,2],[4,5],[7,8],[9,10],[11,12]]
print(spiralOrder(matrix))

