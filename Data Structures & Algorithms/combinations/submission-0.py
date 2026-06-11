from typing import List 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack(start,curr):
            if len(curr)==k:
                res.append(curr.copy())
                return 

            for num in range(start,n+1):
                curr.append(num)
                backtrack(num+1,curr)
                curr.pop()
        backtrack(1, [])
        return res

        