# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curNewNode = None
        curNode1 = list1
        curNode2 = list2
        while ((curNode1 != None) or (curNode2 != None)):
            if curNode1 == None and curNode2 != None:
                newNode = ListNode(curNode2.val)
                curNode2 = curNode2.next
            elif curNode2 == None and curNode1 != None:
                newNode = ListNode(curNode1.val)
                curNode1 = curNode1.next
            elif curNode1.val <= curNode2.val:
                newNode = ListNode(curNode1.val)
                curNode1 = curNode1.next
            else:
                newNode = ListNode(curNode2.val)
                curNode2 = curNode2.next
            
            print(newNode.val)
            if curNewNode == None:
                curNewNode = newNode
                head = curNewNode
            else:
                curNewNode.next = newNode
                curNewNode = curNewNode.next
        
        return head
            

                
                