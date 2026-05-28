# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with negative infinity because node values can be negative
        res = float('-inf')
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            # 1. Recursively find the max path sum of left and right subtrees
            # If the path sum is negative, we split/ignore it by taking max with 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # 2. Compute the max path sum WITH a split at the current node
            # This handles the case where the current node is the highest peak of the path
            current_path_sum = node.val + left_max + right_max
            res = max(res, current_path_sum)
            
            # 3. Return the maximum single path sum (WITHOUT splitting) to the parent
            return node.val + max(left_max, right_max)
            
        dfs(root)
        return res