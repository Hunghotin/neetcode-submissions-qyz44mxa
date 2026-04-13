# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reorder(head):
            start = head
            nxt_s = start
            end = None
            if not head:
                return None
            fast = head.next
            slow = head

            if fast!=None:
                while fast.next!=None:
                    fast = fast.next
                    slow = slow.next
                slow.next = None
                nxt_s = start.next
                start.next = fast
                fast.next = reorder(nxt_s)
            return start
        
        reorder(head)




