class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[["."]* n for _ in range(n)]
        cols=set()
        pos_dig=set()
        neg_dig=set()
        def backtrack(r):

            if r == n:
                copy=["".join(row)for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in cols or (r+c) in pos_dig or (r-c) in neg_dig:
                    continue 
                cols.add(c)
                pos_dig.add(r+c)
                neg_dig.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                cols.remove(c)
                pos_dig.remove(r + c)
                neg_dig.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res


