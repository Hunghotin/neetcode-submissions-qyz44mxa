# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1
        r = list2
        head = ListNode()
        curr = head

        while l and r:
            if l.val<=r.val:
                curr.next = l
                l = l.next
            elif l.val>r.val:
                curr.next = r
                r = r.next
            curr = curr.next

        if l!=None:
            curr.next = l
        if r!=None:
            curr.next = r
        
        return head.next
        