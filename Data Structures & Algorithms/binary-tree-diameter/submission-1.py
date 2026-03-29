
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 
        def dfs(root) :
            nonlocal diameter
            if not root:
                return 0 
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return diameter