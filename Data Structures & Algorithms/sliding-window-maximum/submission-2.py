class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        curr_sum=max(nums[:k])
        res=[curr_sum]
        for i in range(k,n):
            leaving=nums[i-k]
            entering=nums[i]
            if entering>curr_sum:
                curr_sum=entering
            elif leaving==curr_sum:
                curr_sum=max(nums[i-k+1:i+1])
            res.append(curr_sum)
        return res
        