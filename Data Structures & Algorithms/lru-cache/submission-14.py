class Node:
    def __init__(self,key,val):
        self.key = key 
        self.val = val 
        self.prev = None
        self.next = None
        


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next,self.right.prev = self.right,self.left

    def remove(self,node):
        prev1= node.prev
        next1 = node.next
        prev1.next,next1.prev = next1,prev1
    
    def insertatEnd(self,node):
        rightprev = self.right.prev
        rightprev.next = node
        node.prev = rightprev
        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertatEnd(node)
            self.cache[key]=node
            return node.val
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value 
            self.remove(node)
        else:
            node = Node(key,value)
        self.insertatEnd(node)
        self.cache[key]=node
        if len(self.cache)>self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
           
     

