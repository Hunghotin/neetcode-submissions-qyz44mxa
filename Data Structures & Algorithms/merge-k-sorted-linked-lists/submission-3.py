# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(alist, blist):
            mlist = ListNode(val=-float('inf'))
            head = mlist
            i, j = alist, blist
            while i and j:
                if i.val<=j.val:
                    head.next=i
                    i = i.next
                else:
                    head.next=j
                    j=j.next
                head=head.next
            while i:
                head.next = i
                i = i.next
                head = head.next
            while j:
                head.next = j
                j = j.next
                head = head.next
            return mlist.next
        res = ListNode(val=-float('inf'))
        for i in range(len(lists)):
            res = merge(res, lists[i])
        return res.next

