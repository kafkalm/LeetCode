#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 61.py
@time: 2019/2/15 015 12:55
@desc:
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    count = 1
    cur = head
    if head == None:
        return None
    while cur.next != None:
        count+=1
        cur = cur.next
    if count==1:
        return head
    k = k % count
    if k == 0:
        return head
    cur = head
    for i in range(count-k-1):
        cur = cur.next
    head_now = cur.next
    cur.next = None
    cur = head_now
    while cur.next != None:
        cur = cur.next
    cur.next = head
    return head_now

l0 = ListNode(0)
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
# l0.next=l1
l1.next=l2
# l2.next=l3
# l3.next=l4
# l4.next=l5
cur = rotateRight(l1,2)
s = ''
while cur.next!=None:
    s += (str(cur.val)+'->')
    cur=cur.next
s += (str(cur.val))
print(s)