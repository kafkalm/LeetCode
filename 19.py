#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 19.py
@time: 2019/1/29 029 17:09
@desc:删除倒数第N个链表节点
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    Nodelist = []
    while head != None:
        Nodelist.append(head)
        head = head.next
    length = len(Nodelist)
    if length - n - 1 >= 0:
        if n != 1:
            Nodelist[length-n-1].next = Nodelist[length-n+1]
            return Nodelist[0]
        else:
            Nodelist[length-n-1].next = None
            return Nodelist[0]
    elif n == length and length>1:
        return Nodelist[1]
    else:
        return None

l1 = ListNode(1)
l2 = ListNode(2)
# l3 = ListNode(3)
# l4 = ListNode(4)
l1.next = l2
# l2.next = l3
# l3.next = l4
print(removeNthFromEnd(l1,1).val)