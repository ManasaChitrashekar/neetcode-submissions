# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is maximun of height of left free or right subtree
        res = 0
        def height(root):
            nonlocal res
            if not root:
                return 0
            lheight = height(root.left)
            rheight = height(root.right)

            res = max(res,lheight+rheight)
            return 1+max(lheight,rheight)     
        height(root)
        return res