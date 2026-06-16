class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count=0
        board=[["."]* n for _ in range(n)]
        cols=set()
        pos_dig=set()
        neg_dig=set()
        def backtrack(r):
            if r==n:
                self.count+=1
                return 
            for c in range(n):
                if c in cols or (r+c) in pos_dig or (r-c) in neg_dig:
                    continue 
                cols.add(c)
                pos_dig.add(r+c)
                neg_dig.add(r-c)
                backtrack(r+1)
                cols.remove(c)
                pos_dig.remove(r+c)
                neg_dig.remove(r-c)
        backtrack(0)
        return self.count
                
            

        