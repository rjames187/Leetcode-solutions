# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # return one for root because root is always a good node
        return 1 + self.rec(root.left, root.val) + self.rec(root.right, root.val)
    
    def rec (self, root: TreeNode, maxVal) -> int:
        if root == None:
            return 0
        
        if root.val >= maxVal:
            if root.val > maxVal:
                maxVal = root.val
            return 1 + self.rec(root.left, maxVal) + self.rec(root.right, maxVal)
        
        return self.rec(root.left, maxVal) + self.rec(root.right, maxVal)
        