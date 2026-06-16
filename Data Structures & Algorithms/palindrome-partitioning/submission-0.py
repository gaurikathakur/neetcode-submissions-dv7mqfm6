from collections import Counter 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def backtrack(start,curr):
            if len(s)==start:
                res.append(list(curr))
                return 
            for end in range(start,len(s)):
                substring=s[start:end+1]
                if substring==substring[::-1]:
                    curr.append(substring)
                    backtrack(end+1,curr)
                    curr.pop()
        backtrack(0,[])
        return res
            
                

                





        