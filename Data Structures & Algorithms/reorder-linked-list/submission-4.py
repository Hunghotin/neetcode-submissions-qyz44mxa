# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reorder(head):
            if not head:
                return None
            start = head
            fast = head.next
            slow = head

            if fast!=None:
                while fast.next!=None:
                    fast = fast.next
                    slow = slow.next
                slow.next = None
                fast.next = reorder(start.next)
                start.next = fast
                
            return start
        
        reorder(head)




