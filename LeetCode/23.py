#!/usr/bin/env python
# encoding: utf-8
'''
@author: kafkal
@contact: 1051748335@qq.com
@software: pycharm
@file: 23.py
@time: 2019/1/30 030 13:58
@desc:合并 k 个排序链表，返回合并后的排序链表。(采用排两个链表的递归方法） 很慢
采用python自带sorted()方法，并使用attrgetter按val排序 很快
'''

from operator import attrgetter

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    # while True:
    #     if None in lists:
    #         lists.remove(None)
    #     else:
    #         break
    if len(lists) > 1:
        l3 = ListNode(0)
        l3_head = l3
        if lists[0] == None and lists[1] == None:
            return None
        elif lists[0] == None and lists[1] != None:
            lists.pop(0)
            return mergeKLists(lists)
        elif lists[0] != None and lists[1] == None:
            lists.pop(1)
            return mergeKLists(lists)
        if lists[0].val != lists[1].val:
            if lists[0].val <= lists[1].val:
                l3.val = lists[0].val
                lists[0] = lists[0].next
            else:
                l3.val = lists[1].val
                lists[1] = lists[1].next
        else:
            l3.val = lists[0].val
            l3.next = lists[0]
            l3 = l3.next
            l3.val = lists[1].val
            lists[0] = lists[0].next
            lists[1] = lists[1].next
        while lists[0] != None and lists[1] != None:
            if lists[0].val <= lists[1].val:
                l3.next = lists[0]
                lists[0] = lists[0].next
                l3 = l3.next
            else:
                l3.next = lists[1]
                lists[1] = lists[1].next
                l3 = l3.next
        if lists[0] == None and lists[1] != None:
            l3.next = lists[1]
        elif lists[0] != None and lists[1] == None:
            l3.next = lists[0]
        lists.pop(0)
        lists[0] = l3_head
        return mergeKLists(lists)
    elif len(lists) == 1:
        return lists[0]
    else:
        return []

def merge(lists):
    sort_list = []
    for i in lists:
        curr = i
        while curr != None:
            sort_list.append(curr)
            curr = curr.next
    sort_list = sorted(sort_list,key = attrgetter('val'))
    for i in range(len(sort_list)):
        if i == len(sort_list)-1 :
            sort_list[i].next = None
        else:
            sort_list[i].next = sort_list[i+1]
    if len(sort_list) > 0:
        return sort_list[0]
    else:
        return None




l1 = ListNode(-1)
l2 = ListNode(5)
l3 = ListNode(11)
l4 = ListNode(6)
l5 = ListNode(10)
l1.next = l2
l2.next = l3
l4.next = l5
lists = [None,l1,None,l4]
# out = mergeKLists(lists)
out = merge(lists)
while out != None:
    print(out.val)
    out = out.next
