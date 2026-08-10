# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        cur = head
        for i in range(left-1):
            prev = cur 
            cur = cur.next 
        begin = prev.next 
        prev1 = None
       
        for i in range(right-left+1):
            nnext = cur.next 
            cur.next = prev1
            prev1 = cur
            cur = nnext
        
        prev.next = prev1
        begin.next = cur
        return dummy.next 
