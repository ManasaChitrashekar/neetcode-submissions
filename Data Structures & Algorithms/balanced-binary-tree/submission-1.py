# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(root):
            if root is None:
                return 0 
            return 1+max(height(root.left),height(root.right))
        lheight = height(root.left)
        rheight = height(root.right)
        if abs(lheight - rheight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)