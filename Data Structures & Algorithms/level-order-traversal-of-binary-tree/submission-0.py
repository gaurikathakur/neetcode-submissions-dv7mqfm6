from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # 1. Handle empty tree case
            return []
            
        ans = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            curr_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # 2. Use 'node', NOT 'root'
                curr_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 3. Append to ans AFTER the level is fully processed
            ans.append(curr_level)
            
        return ans # 4. Return outside the while loop



        