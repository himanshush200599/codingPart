# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        prev = head
        forw = head.next
        while forw is not None:
            if prev.val == forw.val:
                forw = forw.next
                prev.next = forw
            else:
                prev = forw
                forw = forw.next
        return head
