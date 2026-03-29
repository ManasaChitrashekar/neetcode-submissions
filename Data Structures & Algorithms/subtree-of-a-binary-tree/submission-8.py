# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p is None and q is None:
                return True
            if p and  q is None:
                return False
            if q and  p is None:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        if root is None or subRoot is None :
            return False
        if isSameTree(root,subRoot):
            return True 
        elif root.left and self.isSubtree(root.left,subRoot):
            return True
        elif root.right and self.isSubtree(root.right,subRoot):
            return True
        return False

        