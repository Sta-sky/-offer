"""
反转链表
"""
class ListNode(object):
    def __init__(self, value=None, next = None, head=None):
        self.value = value
        self.next = next
        self.head = head

class Link:
    def pre(self, links):
        if links is None or links.next is None:
            return links
        head = links.head
        per = None
        if head is not None:
            cur = head.next
            head.next = per
            per = head
            head = cur
        return links







