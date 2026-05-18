# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #divide array into two parts
        #rverese second part
        #for reverse lst attach in between every node of fisrt

        slow,fast = head,head.next
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next 
        
        second = slow.next
        #once finding mid point discoonect and create two list 
        slow.next = None
        #rverese second part
        prev = None
        while second:
            tmp = second.next
            second.next=prev
            prev=second
            second = tmp

        list1,list2 = head,prev

        while list2:
            l1next,l2next = list1.next,list2.next
            list1.next = list2
            list2.next = l1next
            list1=l1next
            list2 =l2next
            


