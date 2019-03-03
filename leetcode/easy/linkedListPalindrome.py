# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # print(head.val)
        # end = head
        # while end.next:
        #     end = end.next
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s[:]==s[::-1]
