def removeNthNodeFromEnd(head,n):
    counter = 1
    first =  head
    second = head
    while counter<=n:
        second = second.next
        counter+=1
    if second is None:
        head.val = head.next.val
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
