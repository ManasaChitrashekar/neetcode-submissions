# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        count = 0 
        cur = head
        while cur :
            cur = cur.next 
            count +=1
        ni = count - n
        if ni == 0:
            return head.next
        cur = dummy
        while ni > 0:
            cur = cur.next 
            ni -=1
        cur.next = cur.next.next
        return dummy.next