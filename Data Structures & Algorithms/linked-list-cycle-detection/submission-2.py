# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if slow:
            fast = slow.next
        else:
            return False

        while slow and fast:
            if fast.next==slow:
                return True
            slow = slow.next
            if fast.next:
                if fast.next.next:
                    fast = fast.next.next
                else:
                    return False
            else:
                return False

        return False

