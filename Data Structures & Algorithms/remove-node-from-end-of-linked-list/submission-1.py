# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = ListNode()
        s.next = head
        t = 0
        pointer = head
        while pointer!=None:
            t+=1
            pointer = pointer.next

        count = -1
        pointer = s
        while True:
            if count == t-n-1:
                l = pointer
            if count == t-n:
                r = pointer
                break
            count+=1
            pointer = pointer.next
        l.next = r.next
        
        return s.next
