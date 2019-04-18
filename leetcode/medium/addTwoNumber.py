# You are given two non-empty linked lists representing two non-negative integers.
#  The digits are stored in reverse order and each of their nodes contain a single digit.
#   Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l,n = ListNode(0)
        carry  = 0
        while l1 or l2 or carry:
            v1,v2  = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry,val = divmod(v1+v2+carry,10)
            n.next = ListNode(val)
            n = n.next
        return l.next
# success-congrats - you just solved first medium problem
