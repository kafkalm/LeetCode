#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 68.py
@time: 2019/2/15 015 15:52
@desc:
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''

def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    temp_words = []
    temp_length = -1
    out = []
    idx = 0
    while True:
        if idx < len(words) and temp_length+len(words[idx])+1 <= maxWidth:
            temp_length = temp_length + len(words[idx]) + 1
            temp_words.append(words[idx])
            idx = idx+1
        else:
            if idx != len(words):
                space_length = maxWidth - temp_length
                space_times = len(temp_words) - 1
                space = [' '] * space_times
                if space_times == 0:
                    space_times = 1
                    space = ['']
                while space_length > 0 :
                    for i in range(space_times):
                        space[i] += ' '
                        space_length -= 1
                        if space_length == 0:
                            break
                s = ''
                for i in range(space_times):
                    s += temp_words.pop(0)
                    s += space.pop(0)
                if temp_words != []:
                    s += temp_words.pop(0)
                out.append(s)
                temp_words = []
                temp_length = -1
            else:
                s = ''
                for i in temp_words:
                    s+=i
                    s+=' '
                s = s.rstrip(' ')
                s += (' '*(maxWidth-len(s)))
                out.append(s)
                break
    return out

words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
maxWidth = 16
print(fullJustify(words,maxWidth))
