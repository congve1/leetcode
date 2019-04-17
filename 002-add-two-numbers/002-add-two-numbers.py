# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rem = 0
        res = ListNode(0)
        p = res
        while l1 or l2 or rem:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rem
            rem = val // 10
            p.next = ListNode(val % 10)
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return res.next
        