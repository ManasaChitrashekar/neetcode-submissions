class Node:
    def __init__(self,key,val):
        self.key = key 
        self.val = val 
        self.prev = None 
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next ,self.right.prev = self.right,self.left
        self.lru = {}
        

    def get(self, key: int) -> int:
        if key in self.lru:
            node = self.lru[key]
            self.remove(node)
            self.insert(node)
            self.lru[key]=node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            self.remove(node)
        newnode = Node(key,value)
        self.insert(newnode)
        self.lru[key]=newnode
        if len(self.lru)> self.capacity:
            nodetoremove = self.left.next 
            del self.lru[nodetoremove.key]
            self.remove(nodetoremove)


    def remove(self,node):
        prevnode = node.prev
        nextnode = node.next 
        prevnode.next,nextnode.prev = nextnode,prevnode

    def insert(self,node):
        rearnode = self.right.prev
        rearnode.next = node
        node.prev = rearnode
        node.next = self.right
        self.right.prev = node
    

        
