# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 is None):
            return list2
        if(list2 is None):
            return list1
        cur1 = list1
        cur2 = list2
        list3=head = ListNode()
        while(cur1 and cur2):
            if(cur1.val <= cur2.val):
                  next1 = cur1.next
                  list3.next = cur1
                  cur1= next1  
            else:
                  next2 = cur2.next
                  list3.next = cur2
                  cur2= next2
            list3 = list3.next      
        if (cur1):
            list3.next = cur1
        if(cur2):
            list3.next = cur2

        return head.next                     
