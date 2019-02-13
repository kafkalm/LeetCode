#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 32.py
@time: 2019/1/31 031 11:23
@desc:给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

想法：使用栈来匹配括号 但是匹配到的'('不弹出 打标记 匹配到的多余的右括号 加入到栈中作为分隔符
例如 ’((()())()'
生成流程:
    stack = ['(','(','(']
    stack = ['(','(','1']
    stack = ['(','(','1','(']
    stack = ['(','(','1','1']
    stack = ['(','1','1','1']
    stack = ['(','1','1','1','(']
    stack = ['(','1','1','1','1']
    统计不被分隔的1的个数
优化：
    采用下标计数 就不需要再遍历stack了
    例如 ’((()())()'
    初始下标 idx = 0
    在栈中保存 '(' 下标
    遇到右括号 弹出1个栈顶的 '(' 栈非空：ans = i - stack[-1] 栈空: ans = i -
    遇到多余的右括号 使 idx = i + 1 即指示了下一个可能为左括号的位置
    计算 idx - 栈中最后一个弹出的'('的下标
    并与保存的最大值进行比较
'''

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    stack = []
    idx = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack != []:
                stack.pop(-1)
                if stack != []:
                    ans = max(ans,i - stack[-1])
                else:
                    ans = max(ans,i - idx + 1)
            else:
                idx = i + 1
    return ans

# s="()(()"
# s="((()))"
# s="((()())"
# s=")()())"
s = ")()())()()("
print(longestValidParentheses(s))