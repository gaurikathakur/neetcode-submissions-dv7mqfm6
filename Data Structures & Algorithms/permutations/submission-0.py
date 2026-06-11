from typing import List 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visited=[False]*len(nums)
        def backtrack(curr):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return 
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i]=True 
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    visited[i]=False 
        backtrack([])
        return res

            


        