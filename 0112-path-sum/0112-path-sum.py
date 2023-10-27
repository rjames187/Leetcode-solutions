# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, path_sum):
            if not root: return False
            path_sum += root.val
            if not (root.left or root.right):
                return path_sum == targetSum
            if dfs(root.left, path_sum):
                return True
            if dfs(root.right, path_sum):
                return True
            return False
        return dfs(root, 0)
        