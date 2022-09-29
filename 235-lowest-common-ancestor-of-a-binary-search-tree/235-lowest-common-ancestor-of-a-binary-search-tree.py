# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p = p.val
        q = q.val
        
        def seek (node):
            if not node:
                return (False, None)
            
            tup_left = seek(node.left)
            tup_right = seek(node.right)
            
            if tup_left[0]:
                return tup_left
            if tup_right[0]:
                return tup_right
            
            
            pool = [node.val, tup_left[1], tup_right[1]]
            
            if p in pool and q in pool:
                return (True, node)
            elif p in pool:
                return (False, p)
            elif q in pool:
                return (False, q)
            else:
                return (False, None)
        
        return seek(root)[1]
            
        
            
            