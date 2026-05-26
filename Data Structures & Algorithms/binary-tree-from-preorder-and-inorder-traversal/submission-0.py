# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={val: idx for idx,val in enumerate(inorder)}
        pre_index=0
        def helper(left_in,right_in):
            nonlocal pre_index
            if left_in>right_in:
                return None 
            root_val=preorder[pre_index]
            root=TreeNode(root_val)
            pre_index+=1
            pivot=inorder_map[root_val]
            root.left=helper(left_in,pivot-1)
            root.right=helper(pivot+1,right_in)
            return root
        return helper(0,len(inorder)-1)




        