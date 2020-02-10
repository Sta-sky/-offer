

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #       迭代的方法
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur

        return prev


link_iist = [2, 4, 5.3, 1]