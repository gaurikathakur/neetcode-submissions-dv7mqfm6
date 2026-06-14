class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visited=[False]*len(nums)
        nums.sort()
        def backtrack(curr):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            i=0
            while i<len(nums):
                if not visited[i]:
                    visited[i]=True 
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    visited[i]=False
                    while i+1<len(nums) and nums[i]==nums[i+1]:
                        i+=1
                i+=1
        backtrack([])
        return res

            


