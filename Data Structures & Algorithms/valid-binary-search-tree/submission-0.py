# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None  # Track previous node value during traversal

        def inorder(node):
            if not node:
                return True
            
            # Check left subtree
            if not inorder(node.left):
                return False
            
            # Check current node value > previous value
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val  # Update previous value
            
            # Check right subtree
            return inorder(node.right)
        
        return inorder(root)
