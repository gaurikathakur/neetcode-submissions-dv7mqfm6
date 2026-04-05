class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        curr_max=max(nums[:k])
        res=[curr_max]
        for i in range(k,n):
            leaving=nums[i-k]
            entering=nums[i]
            if entering>=curr_max:
                curr_max=entering 
            elif leaving==curr_max:
                curr_max=max(nums[i-k+1:i+1])
            res.append(curr_max)
        return res

