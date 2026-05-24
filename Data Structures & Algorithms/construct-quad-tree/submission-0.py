class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(r, c, n):
            # 1. Check if all values in the current sub-grid are identical
            all_same = True
            first_val = grid[r][c]
            
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break
            
            # 2. Base Case: If uniform, return a leaf node
            if all_same:
                return Node(val=bool(first_val), isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            
            # 3. Otherwise, split into 4 quadrants evenly
            half = n // 2
            top_left = dfs(r, c, half)
            top_right = dfs(r, c + half, half)
            bottom_left = dfs(r + half, c, half)
            bottom_right = dfs(r + half, c + half, half)
            
            # 4. Return internal node pointing to the 4 child quadrants
            return Node(
                val=True, 
                isLeaf=False, # Must be False for internal nodes
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bottom_left,
                bottomRight=bottom_right
            )
            
        return dfs(0, 0, len(grid))