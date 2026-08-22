class MyHashSet:

    def __init__(self):
        self.hmap = {}

    def add(self, key: int) -> None:
        self.hmap[key]= key

    def remove(self, key: int) -> None:
        if key in self.hmap:
            del self.hmap[key]

    def contains(self, key: int) -> bool:
        if key in self.hmap:
            return True 
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)