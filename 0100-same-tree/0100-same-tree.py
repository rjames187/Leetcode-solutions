# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p, q)]
        while len(queue):
            cur_p, cur_q = queue.pop(0)
            if cur_p == None and cur_q == None:
                # we can skip
                continue
            if (not cur_p) or (not cur_q):
                return False
            if cur_p.val != cur_q.val:
                return False
            queue.append((cur_p.left, cur_q.left))
            queue.append((cur_p.right, cur_q.right))
        return True
        
        