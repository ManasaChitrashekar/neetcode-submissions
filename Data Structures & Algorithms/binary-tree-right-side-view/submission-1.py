# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        pqueue = collections.deque()
        if root :
            pqueue.append(root)

        while(pqueue):
            lenCounter = len(pqueue)
            rightSide = None
            for i in range(lenCounter):
                node = pqueue.popleft()
                if node :
                    rightSide = node
                    pqueue.append(node.left)
                    pqueue.append(node.right)  
            if rightSide:        
                res.append(rightSide.val)
        return res     
        