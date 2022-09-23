# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(node):
            if node == None:
                return 0
            if node.right == None and node.left == None:
                return 1
            else:
                left = recurse(node.left)
                right = recurse(node.right)
                #print(left, right)
                if left - right > 1 or left - right < - 1:
                    return False
                if (left == False and not(type(left) is int)) or (right == False and not(type(right) is int)):
                    return False
                return max(left + 1, right + 1)
        
        result = recurse(root)
        if(result != False or type(result) is int):
            return True
        else:
            return False
        