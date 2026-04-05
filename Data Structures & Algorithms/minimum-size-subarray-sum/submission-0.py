from collections import defaultdict
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        curr_sum=0
        l=0
        min_sum=float('inf')
        for right in range (len(nums)):
            curr_sum+=nums[right]

            while curr_sum>=target:

                min_sum=min(min_sum,right-l+1)
                curr_sum -= nums[l]
                l += 1
        return int(min_sum) if min_sum != float('inf') else 0

