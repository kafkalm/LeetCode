#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 24.py
@time: 2019/1/30 030 14:29
@desc:给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    nodes = []
    out_nodes = []
    if head != None and head.next != None:
        curr = head
        while curr != None:
            nodes.append(curr)
            curr = curr.next
        max_len = len(nodes)
        if max_len != 2:
            if max_len % 2 != 0 and max_len % 2 != 2:
                times = max_len // 2
            else:
                times = max_len // 2 - 1
            for i in range(times):
                try:
                    nodes_swap = nodes[2 * i:2 * i + 4]
                except:
                    nodes_swap = nodes[2 * i:]
                nodes_swap[1].next = nodes_swap[0]
                nodes_swap[0].next = nodes_swap[-1]
                nodes_swap[-1].next = nodes_swap[2]
                nodes_swap[2].next = None
                out_nodes.extend(nodes_swap)
            return out_nodes[1]
        else:
            nodes[1].next = nodes[0]
            nodes[0].next = None
            return nodes[1]
    elif head != None and head.next == None:
        return head
    else:
        return None

def swapPairs_2(head):
    if head == None or head.next == None:
        return head
    g = None
    Head = head.next

    while head != None and head.next != None:
        t = head.next.next
        if g != None:
            g.next = head.next
        head.next.next = head
        head.next = t
        g = head
        head = t

    return Head

l1 = ListNode(-1)
l2 = ListNode(5)
l3 = ListNode(11)
l4 = ListNode(6)
l5 = ListNode(10)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
out = swapPairs(l1)
while out != None:
    print(out.val)
    out = out.next