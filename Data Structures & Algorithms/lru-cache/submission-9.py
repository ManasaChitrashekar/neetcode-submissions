class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cmap = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cmap:
            node = self.cmap[key]
            self.removeFront(node)
            self.insertLast(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cmap:
            self.removeFront(self.cmap[key])

        node = ListNode(key, value)
        self.cmap[key] = node
        self.insertLast(node)

        if len(self.cmap) > self.capacity:
            lru = self.left.next
            self.removeFront(lru)
            del self.cmap[lru.key]

    def removeFront(self, node):
        prev1 = node.prev
        next1 = node.next 
        prev1.next = next1
        next1.prev = prev1
    
    def insertLast(self, node):
        prev1 = self.right.prev
        prev1.next = node
        node.prev = prev1
        node.next = self.right
        self.right.prev = node