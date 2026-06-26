# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root:
            return "N"
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        datalist = data.split(",")
        if datalist[0]=="N":
            return None
        root = TreeNode(datalist[0])
        q = deque()
        q.append(root)
        index = 1
        while q:
            node =q.popleft()
            if datalist[index]!="N":
                leftnode = TreeNode(datalist[index])
                
                node.left =leftnode
                q.append(leftnode)
            index +=1
            if datalist[index]!="N":
                rightnode = TreeNode(datalist[index])
                node.right = rightnode
                q.append(rightnode)
            index +=1
        return root
            