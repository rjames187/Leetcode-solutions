# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        p1 = list1
        p2 = list2
        if list1.val < list2.val:
            head = ListNode(list1.val)
            p1 = p1.next
        else:
            head = ListNode(list2.val)
            p2 = p2.next
        
        new_list = head
        while p1 != None or p2 != None:
            if p1 == None:
                new_list.next = ListNode(p2.val)
                new_list = new_list.next
                p2 = p2.next
            elif p2 == None:
                new_list.next = ListNode(p1.val)
                new_list = new_list.next
                p1 = p1.next
            elif p1.val < p2.val:
                new_list.next = ListNode(p1.val)
                new_list = new_list.next
                p1 = p1.next
            else:
                new_list.next = ListNode(p2.val)
                new_list = new_list.next
                p2 = p2.next
            
        return head
                
                