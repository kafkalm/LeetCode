#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 49.py
@time: 2019/2/14 014 10:26
@desc:
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    ans = {}
    out = []
    for i in strs:
        count = [0] * 26
        for c in i:
            count[ord(c) - ord('a')] +=1
        if ans.get(tuple(count)):
            ans[tuple(count)].append(i)
        else:
            ans[tuple(count)] = [i]
    # for v in ans.values():
    #     out.append(v)
    return list(ans.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))