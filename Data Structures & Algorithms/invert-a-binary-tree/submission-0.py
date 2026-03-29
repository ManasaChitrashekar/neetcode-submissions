# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pqueue = collections.deque()
        if root:
            pqueue.append(root)
        while(pqueue):
            node = pqueue.popleft()
            node.left,node.right = node.right,node.left
            if node.left:
                pqueue.append(node.left) 
            if node.right:
                pqueue.append(node.right) 
        return root