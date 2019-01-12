# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if  head is None or head.next is None:
            return False
        head1  = head.next
        while head!=head1:
            if head1 is None or head1.next is None:
                return False
            head = head.next
            head1 = head1.next.next
        return True
