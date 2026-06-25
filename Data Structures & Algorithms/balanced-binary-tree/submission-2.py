# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightbalanced(root):
            if not root:
                return 0
            lefth = heightbalanced(root.left)
            if lefth == -1:
                return -1
            righth = heightbalanced(root.right)
            if righth == -1:
                return -1
            if abs(lefth-righth)>1:
                return -1
            return 1+max(lefth,righth)
        return heightbalanced(root) !=-1