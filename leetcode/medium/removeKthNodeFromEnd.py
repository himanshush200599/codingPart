# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        counter = 1
        first =  head
        second = head
        if head.next is None and n==1:
            return []
        while counter<=n:
            second = second.next
            counter+=1
        if second is None:
            head.val = head.next.val
            head.next = head.next.next
            return  head
        while second.next is not None:
            second = second.next
            first = first.next
        first.next = first.next.next
        return head
