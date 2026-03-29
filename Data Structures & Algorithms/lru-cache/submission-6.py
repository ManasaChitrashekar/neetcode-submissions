class DNode:
    def __init__(self, key, val):   # ✅ should be __init__, not _init_
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # ✅ HashMap: key -> node

        # ✅ Dummy head and tail to simplify insert/remove
        self.head, self.tail = DNode(0, 0), DNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        """Remove node from DLL"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        """Insert node right after head (most recent position)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # Move the accessed node to the front
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # If key already exists, remove it
        if key in self.cache:
            self.remove(self.cache[key])

        # Insert new node
        node = DNode(key, value)
        self.cache[key] = node
        self.insert(node)

        # If over capacity, remove LRU (tail.prev)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
