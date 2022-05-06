import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.lastNode = -math.inf
        self.is_valid = True
        
        def inOrder (aNode):
            if (aNode != None):
                inOrder (aNode.left)
                #print(aNode.val, self.lastNode)
                if aNode.val <= self.lastNode:
                    self.is_valid = False
                else:
                    self.lastNode = aNode.val
                inOrder (aNode.right)
        
        inOrder(root)
        return self.is_valid
    