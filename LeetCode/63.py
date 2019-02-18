#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 63.py
@time: 2019/2/15 015 13:22
@desc:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

[
  [0,1,0,0],
  [0,1,1,0],
  [0,0,0,0]
]

动态规划
'''

nums =[[0,1]]


#递归超时
def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    count = []
    def dp(i, j):
        if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
            count.append(1)
        if obstacleGrid[i - 1][j] == 0 and i > 0:
            dp(i - 1, j)
        if obstacleGrid[i][j - 1] == 0 and j > 0:
            dp(i, j - 1)
    if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:
        return 0
    dp(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
    return len(count)

#动态规划
def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    map = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
    def dp(i, j):
        if map[i][j] != -1:
            return map[i][j]
        c = 0
        if i == 0 and j == 0 and obstacleGrid[i][j] != 1:
            c = 1
        if obstacleGrid[i - 1][j] == 0 and i > 0:
            c += dp(i - 1, j)
        if obstacleGrid[i][j - 1] == 0 and j > 0:
            c += dp(i, j - 1)
        map[i][j] = c
        return c
    if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:
        return 0
    return dp(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
print(uniquePathsWithObstacles(nums))


