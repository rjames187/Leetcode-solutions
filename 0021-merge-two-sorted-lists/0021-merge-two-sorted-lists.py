# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = None
        while list1 or list2:
            selected = None
            if not list1:
                selected = list2
                list2 = list2.next
            elif not list2:
                selected = list1
                list1 = list1.next
            elif list1.val < list2.val:
                selected = list1
                list1 = list1.next
            else:
                selected = list2
                list2 = list2.next
            selected.next = None
            if not cur:
                cur, head = selected, selected
            else:
                cur.next = selected
                cur = cur.next
        return head
                
        