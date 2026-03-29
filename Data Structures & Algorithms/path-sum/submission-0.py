# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,sum):
            if root is None:
                return False
            sum = sum + root.val 
            if not root.left and not root.right:
                return sum == targetSum
            if dfs(root.left,sum):
                return True 
            if dfs(root.right,sum):
                return True
            return False
        return dfs(root,0)