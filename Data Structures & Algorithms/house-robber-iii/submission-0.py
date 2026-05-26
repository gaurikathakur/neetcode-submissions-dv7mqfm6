# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0,0]
            left_choices=dfs(node.left)
            right_choices=dfs(node.right)
            rob_this=node.val+left_choices[1]+right_choices[1]
            skip_this=max(left_choices)+ max(right_choices)
            return[rob_this,skip_this]
        return max(dfs(root))


        