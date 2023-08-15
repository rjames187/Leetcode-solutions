# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        cur_lvl = []
        while len(q):
            lvl_size = len(q)
            for i in range(lvl_size):
                node = q.pop(0)
                cur_lvl.append(node.val)
                for new_node in [node.left, node.right]:
                    if new_node:
                        q.append(new_node)
            res.insert(0, cur_lvl)
            cur_lvl = []
        return res