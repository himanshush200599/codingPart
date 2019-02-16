# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseList(self, head):
        pre = None
        cur = head

        while cur:
            nextTemp = cur.next
            cur.next = pre
            pre = cur
            cur = nextTemp

        return pre
