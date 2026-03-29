# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        pqueue = collections.deque()
        if root :
            pqueue.append(root)

        while(pqueue):
            lenCounter = len(pqueue)
            lis= []
            for i in range(lenCounter):
                node = pqueue.popleft()
                if node :
                    pqueue.append(node.left)
                    pqueue.append(node.right)  
                    lis.append(node.val)  
            if lis:        
                res.append(lis)
        return res    