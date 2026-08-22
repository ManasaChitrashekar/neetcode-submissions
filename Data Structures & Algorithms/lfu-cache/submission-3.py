class Node:
    def __init__(self,key,val):
        self.key = key 
        self.val = val 
        self.prev = None 
        self.next = None
        self.freq = 1
class Dlist:
    def __init__(self):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next,self.right.prev= self.right,self.left

    def insertrear(self,node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def remove(self,node):
        prev = node.prev
        nextnode = node.next 
        prev.next ,nextnode.prev = nextnode,prev

    def is_empty(self):
        return self.left.next == self.right


class LFUCache:

    def __init__(self, capacity: int):
        self.lfu_cache = {}
        self.freq_list = defaultdict(Dlist)
        self.capacity = capacity 
        self.minfreq = 0 
        
    def get(self, key: int) -> int:
        if key not in self.lfu_cache :
            return -1
        node = self.lfu_cache[key]
        self.updateFreqMap(node)
        return node.val

    def updateFreqMap(self,node):
        freq = node.freq
        dlist = self.freq_list[freq]
        dlist.remove(node)

        if dlist.is_empty() and freq == self.minfreq :
            self.minfreq +=1
        node.freq +=1
        self.freq_list[node.freq].insertrear(node)
        

    def put(self, key: int, value: int) -> None:
        if key in self.lfu_cache :
            node = self.lfu_cache[key]
            node.val = value
            self.updateFreqMap(node)
            return
        else:
            if len(self.lfu_cache) == self.capacity :
                mincountlist = self.freq_list[self.minfreq]
                lru = mincountlist.left.next 
                mincountlist.remove(lru)
                del self.lfu_cache[lru.key]
            node = Node(key,value)
            self.lfu_cache[key]= node
            self.freq_list[node.freq].insertrear(node)
            self.minfreq =1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)