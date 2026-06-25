# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxpathsum = float("-inf")
        def dfs(root):
            if not root :
                return 0
            lsum = max(dfs(root.left),0)
            rsum = max(dfs(root.right),0)
            self.maxpathsum = max(self.maxpathsum,root.val+lsum+rsum)

            return root.val+max(lsum,rsum)
        dfs(root)
        return self.maxpathsum