#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 25.py
@time: 2019/1/30 030 15:13
@desc:给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
采取24题列表法
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
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
        if max_len < k:
            return head
        if max_len > k:
            if max_len % k == 0:
                times = max_len // k - 1
            else:
                times = max_len // k
            for i in range(times):
                nodes_swap = nodes[k * i:k * i + 2*k]
                if len(nodes_swap) % k == 0:
                    for i in range(len(nodes_swap)):
                        if i == k - 1:
                            nodes_swap[-1-i].next = None
                        elif i == 2*k -1:
                            nodes_swap[-1-i].next = nodes_swap[-1]
                        else:
                            nodes_swap[-1 - i].next = nodes_swap[-2 - i]
                    out_nodes.extend(nodes_swap)
                else:
                    for i in range(len(nodes_swap) - len(nodes_swap) % k - 1):
                        nodes_swap[-1 - i-len(nodes_swap)%k].next = nodes_swap[-2 - i-len(nodes_swap)%k]
                    nodes_swap[0].next = nodes_swap[len(nodes_swap) % k + 1]
                    out_nodes.extend(nodes_swap)
            return out_nodes[k-1]
        else:
            for i in range(max_len-1):
                nodes[-1-i].next = nodes[-2-i]
            nodes[0].next = None
            return nodes[1]
    elif head != None and head.next == None:
        return head
    else:
        return None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
out = reverseKGroup(l1,3)
while out != None:
    print(out.val)
    out = out.next