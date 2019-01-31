#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 21.py
@time: 2019/1/29 029 17:46
@desc:排序两个有序链表
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l3 = ListNode(0)
    l3_head = l3
    if l1 == None and l2 == None:
        return None
    elif l1 == None and l2 != None:
        return l2
    elif l1 != None and l2 == None:
        return l1
    if l1.val != l2.val:
        if l1.val <= l2.val:
            l3.val = l1.val
            l1 = l1.next
        else:
            l3.val = l2.val
            l2 = l2.next
    else:
        l3.val = l1.val
        l3.next = l1
        l3 = l3.next
        l3.val = l2.val
        l1 = l1.next
        l2 = l2.next
    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            l3.next = l1
            l1 = l1.next
            l3 = l3.next
        else:
            l3.next = l2
            l2 = l2.next
            l3 = l3.next
    if l1 == None and l2 != None:
        l3.next = l2
    elif l1 != None and l2 == None:
        l3.next = l1
    return l3_head

l1 = ListNode(1)
l3 = ListNode(3)
l4 = ListNode(4)

l2 = ListNode(2)
l5 = ListNode(5)
l6 = ListNode(6)

l1.next = l3
l3.next = l5

l2.next = l4
l4.next = l6
mergeTwoLists(l1,l2)