# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if  not headA or not headB:
            return None

        a = headA
        b = headB

        while a != b:
            if a is not None:
                a = a.next
            else:
                a = headB
            if b is not None:
                b = b.next
            else:
                b = headA

        return a
