# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
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
        
        def find(root, subRoot):
            res = 0
            if not root:
                return 0
            if root.val==subRoot.val:
                if isSameTree(root, subRoot):
                    return 1
            res = find(root.left, subRoot)
            print(res)
            res = max(res, find(root.right,subRoot))
            return res
        
        if find(root, subRoot)==1:
            return True
        else:
            return False