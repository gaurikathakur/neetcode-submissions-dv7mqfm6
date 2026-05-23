from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        queue=deque([root])
        while queue:
            level_size=len(queue)
            curr_level=[]
            for _ in range(level_size):
                node=queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curr_level)
        return ans

