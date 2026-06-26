# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder,inorder):
            if not (preorder or inorder):
                return None
            root = TreeNode()
            rvalue = preorder[0]
            root.val = rvalue
            rindex = inorder.index(rvalue)
            root.left = dfs(preorder[1:rindex+1],inorder[:rindex])
            root.right = dfs(preorder[rindex+1:],inorder[rindex+1:])

            return root
        return dfs(preorder,inorder)