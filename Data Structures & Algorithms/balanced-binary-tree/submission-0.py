# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getheight(node):
            if not node:
                return 0
            left=getheight(node.left)
            if left == -1:
                return -1
            right=getheight(node.right)
            if right==-1:
                return -1
            if abs(left - right) > 1:
                return -1
            
            # 5. Return height: Must return an integer for the parent to use
            return 1 + max(left, right)
        return getheight(root) != -1