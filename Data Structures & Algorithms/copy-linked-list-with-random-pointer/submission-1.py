"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        nodemap = {None:None}
        #create nodes for each orginal node and cretae mapping
        while cur:
            newnode = Node(cur.val)
            nodemap[cur] = newnode
            cur = cur.next 
        cur = head 
        #after all duplicate nodes are created now establish link for each copy node usein copy of original next an random
        while cur:
            copy = nodemap[cur]
            copy.next = nodemap[cur.next]
            copy.random = nodemap[cur.random]
            cur = cur.next
        return nodemap[head]