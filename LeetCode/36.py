#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 36.py
@time: 2019/2/13 013 10:07
@desc:
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
'''


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    test = []
    k = 0
    for j in range(9):
        col = []
        for l in board:
            for i in range(9):
                if l[i] == '.':
                    continue
                else:
                    a = l.pop(i)
                    if a in l:
                        return False
                    else:
                        l.insert(i,a)
                        continue
            col.append(l[k])
        k+=1
        test.append(col)
    for j in range(0,9,3):
        box = []
        for l in board[j:j+3]:
            box.extend(l[0:3])
        test.append(box)
        box = []
        for l in board[j:j+3]:
            box.extend(l[3:6])
        test.append(box)
        box = []
        for l in board[j:j + 3]:
            box.extend(l[6:9])
        test.append(box)
    for l in test:
        for i in range(9):
            if l[i] == '.':
                continue
            else:
                a = l.pop(i)
                if a in l:
                    return False
                else:
                    l.insert(i, a)
                    continue
    return True

board =[[".","2",".",".",".",".",".",".","."],
        [".",".",".",".",".",".","5",".","1"],
        [".",".",".",".",".",".","8","1","3"],
        ["4",".","9",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".","2",".",".",".",".",".","."],
        ["7",".","6",".",".",".",".",".","."],
        ["9",".",".",".",".","4",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
print(isValidSudoku(board))