#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 5.py
@time: 2019/1/28 028 11:15
@desc:
'''

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    max_len = 0
    max_s = ''
    max_s_2 = ''
    out = ''
    for i in range(0,len(s)-1):
        if i != 0 and s[i - 1] == s[i + 1] and s[i] != s[i+1]:
            new_s = s[i - 1:i + 2]
            new_len = 3
            if max_len < new_len:
                max_s = new_s
            try:
                for j in range(2, min(i, len(s) - i - 1) + 1):
                    if s[i - j] == s[i + j]:
                        new_s = s[i - j:i + j + 1]
                        new_len = len(new_s)
                        if max_len < new_len:
                            max_len = new_len
                            max_s = new_s
                    else:
                        break
            except:
                pass
        elif s[i] == s[i+1] and s[i-1] != s[i+1]:
            new_s = s[i:i+2]
            new_len = 2
            if max_len < new_len:
                max_s = new_s
            try:
                for j in range(1,min(i,len(s)-i-1)+1):
                    if s[i-j] == s[i+(new_len//2)+1]:
                        new_s = s[i-j:i+(new_len//2)+2]
                        new_len = len(new_s)
                        if max_len < new_len:
                            max_len = new_len
                            max_s = new_s
                    else:
                        break
            except:
                pass
        elif s[i-1]==s[i] and s[i] == s[i+1]:
            new_s = s[i - 1:i + 2]
            new_len = 3
            if max_len < new_len:
                max_s = new_s
            try:
                for j in range(2, min(i, len(s) - i - 1) + 1):
                    if s[i - j] == s[i + j]:
                        new_s = s[i - j:i + j + 1]
                        new_len = len(new_s)
                        if max_len < new_len:
                            max_len = new_len
                            max_s = new_s
                    else:
                        break
            except:
                pass

            new_s = s[i:i + 2]
            new_len = 2
            if max_len < new_len:
                max_s_2 = new_s
            try:
                for j in range(1, min(i, len(s) - i - 1) + 1):
                    if s[i - j] == s[i + (new_len // 2) + 1]:
                        new_s = s[i - j:i + (new_len // 2) + 2]
                        new_len = len(new_s)
                        if max_len < new_len:
                            max_len = new_len
                            max_s_2 = new_s
                    else:
                        break
            except:
                pass

    if len(max_s)<=len(max_s_2):
        out = max_s_2
    else:
        out = max_s
    if max_s == '' and s != '' and max_s_2 == '':
        out = s[0]
    elif s == '':
        out = ''
    return max_s
s = 'aaa'

print(len(s))
print(longestPalindrome(s))