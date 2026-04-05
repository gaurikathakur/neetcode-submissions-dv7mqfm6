import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Initialize hash sets to track seen numbers
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                # 2. Skip empty cells
                if board[r][c] == ".":
                    continue

                val = board[r][c]
                # 3. Use (r // 3, c // 3) to identify which 3x3 box we are in
                square_key = (r // 3, c // 3)

                # 4. Check for duplicates in current row, column, or square
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[square_key]):
                    return False 

                # 5. Add current number to trackers
                rows[r].add(val)
                cols[c].add(val)
                squares[square_key].add(val)
        
        # 6. Return True only AFTER checking all cells
        return True







        