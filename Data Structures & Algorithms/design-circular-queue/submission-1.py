class ListNode:
    def __init__(self,val,next,prev):
        self.val,self.next,self.prev = val,next,prev
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.left = ListNode(0,None,None)
        self.right = ListNode(0,None,self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.k -=1
        prev = self.right.prev
        node = ListNode(value,self.right,self.right.prev)
        prev.next = node 
        self.right.prev = node
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        cur = self.left.next
        self.left.next = cur.next
        cur.next.prev = self.left
        self.k +=1
        return True
        

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        #only 2 varibales
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.k == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()