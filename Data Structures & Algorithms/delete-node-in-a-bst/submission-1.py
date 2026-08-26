# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key< root.val :
            root.left = self.deleteNode(root.left,key)
        elif key > root.val :
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left :
                return root.right
            elif not root.right:
                return root.left 
            #find min to make root node by picking the min val from right subtree
            cur = root.right
            while cur.left:
                cur= cur.left 
            #now existing left min val that we can make as root 
            root.val =cur.val
            #as now there are two duplicates in nodes we delete one from right subtree
            root.right = self.deleteNode(root.right,root.val)
        return root