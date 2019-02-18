#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 64.py
@time: 2019/2/15 015 14:15
@desc:
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

动态规划
'''

def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if grid == []:
        return 0
    map = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    def dp(i,j):
        if map[i][j] != -1:
            return map[i][j]
        if i == len(grid)-1 and j == len(grid[0])-1:
            map[i][j] = grid[i][j]
        elif i+1 <len(grid) and j+1 < len(grid[0]):
            map[i][j] = grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))
        elif i+1 <len(grid) and j == len(grid[0])-1:
            map[i][j] = grid[i][j] + dp(i + 1, j)
        elif i == len(grid)-1 and j+1 < len(grid[0]):
            map[i][j] = grid[i][j] + dp(i, j + 1)
        return map[i][j]
    dp(0,0)
    return map[0][0]

grid = [[9,1,4,8]]
print(minPathSum(grid))
