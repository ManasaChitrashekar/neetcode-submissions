class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1        # every new node starts at frequency 1
        self.prev = None
        self.next = None

class DList:
    def __init__(self):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next  = self.right
        self.right.prev = self.left

    def pushRight(self,node):
        prev1 = self.right.prev
        
        prev1.next = node
        node.prev = prev1

        node.next =self.right
        self.right.prev = node

    def removeNode(self,node):
        prev1,next1 = node.prev, node.next 

        prev1.next = next1
        next1.prev = prev1

        node.next,node.prev = None,None

    def is_empty(self):
        return self.left.next == self.right

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.nmap = {}
        self.countmap = defaultdict(DList)
        self.minfreq = 0

    def get(self, key: int) -> int:
        if key not in self.nmap:
            return -1 
        node = self.nmap[key]
        self.updateFreqMap(node)
        return node.val

    def updateFreqMap(self,node):
        freq = node.freq
        countlist = self.countmap[freq]
        countlist.removeNode(node)

        if countlist.is_empty() and freq==self.minfreq:
            self.minfreq +=1
        node.freq +=1
        self.countmap[node.freq].pushRight(node)


    def put(self, key: int, value: int) -> None:
        if key in self.nmap:
            self.nmap[key].val = value
            self.updateFreqMap(self.nmap[key]) 
        else:
            if len(self.nmap)==self.cap:
                mincountlist = self.countmap[self.minfreq]
                lru = mincountlist.left.next
                mincountlist.removeNode(lru)
                del self.nmap[lru.key]

            node = Node(key,value)
            self.nmap[key] = node
            self.minfreq = 1
            self.countmap[1].pushRight(node)


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)