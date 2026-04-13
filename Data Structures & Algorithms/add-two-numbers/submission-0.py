# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        s = ListNode(0)
        sp = s
        tmp=0

        while True:
            a = 0 if p1==None else p1.val
            b = 0 if p2==None else p2.val
        
            if a+b+tmp<10:
                sp.val = a+b+tmp
                tmp = 0
            elif a+b+tmp>=10:
                sp.val = a+b+tmp-10
                tmp = 1

            if p1!=None:
                p1 = p1.next
            if p2!=None:
                p2 = p2.next
            print(tmp)
            if tmp>0 or p1!=None or p2!=None:
                sp.next = ListNode(0)
                sp = sp.next
            else:
                sp.next = None
                break
        
        return s
        
