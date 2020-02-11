# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
获取链表的所有值加入列表中 直到节点对象的next值未空时为止   最后取出第k个值

"""


class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <1:
            return None

        list_ = []
        cur = head
        while cur:
            list_.append(cur)
            cur = cur.next
        if k > len(list_):
            return None
        return list_[-k]