# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is empty, it's technically a subtree of any tree
        if not subRoot: 
            return True
        # If root is empty but subRoot isn't, subRoot can't be a subtree
        if not root: 
            return False
        
        # 1. Check if the trees starting at current nodes are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. Otherwise, recursively check the left and right children of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are identical
        if not p and not q:
            return True
        
        # If one is None or values differ, they aren't identical
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)