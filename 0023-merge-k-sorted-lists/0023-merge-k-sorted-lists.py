from heapq import heapify, heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # variables
        head = None
        pointer = None
        h = []
        
        # initialize heap
        for i in range(len(lists)):
            ll = lists[i]
            if not ll:
                continue
            h.append((ll.val, i))
            lists[i] = ll.next
        heapify(h)
        
        # sort
        while (len(h)):
            popped = heappop(h)
            val = popped[0]
            if not pointer:
                head = ListNode(val)
                pointer = head
            else:
                pointer.next = ListNode(val)
                pointer = pointer.next
            
            i = popped[1]
            ll = lists[i]
            if ll:
                heappush(h, (ll.val, i))
                lists[i] = ll.next
        
        return head
            
            
            
            
            
            
        
        
        