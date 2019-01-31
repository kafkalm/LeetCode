#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 6.py
@time: 2019/1/28 028 17:09
@desc:
'''

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    else:
        L = []
        idx = numRows
        for i in range(numRows):
            L.append([])
        trans_times = 1 + (len(s) - numRows) // (numRows - 1)
        for i in range(numRows):
            if i < len(s):
                L[i].append(s[i])
            else:
                break
        for i in range(trans_times):
            if i % 2 == 0:
                for j in range(numRows-1):
                    if idx < len(s):
                        L[numRows-j-2].append(s[idx])
                        idx += 1
            else:
                for j in range(numRows-1):
                    if idx < len(s):
                        L[j+1].append(s[idx])
                        idx += 1
        out = ''
        for l in L:
            out = out + ''.join(l)
    return out

print(convert('A',2))

