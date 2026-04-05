class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                corr_idx=nums[i]-1
                nums[i],nums[corr_idx]=nums[corr_idx],nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:

                return i + 1
        return n+1
        

        