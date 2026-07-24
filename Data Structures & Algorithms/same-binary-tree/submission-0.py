# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        plist = []
        qlist = []
        def record(head, mem):
            if head==None:
                mem.append(None)
                return mem
            
            mem.append(head.val)
            mem = record(head.left, mem)
            mem = record(head.right, mem)

            return mem
        
        if record(p, plist) == record(q, qlist):
            return True
        else:
            return False