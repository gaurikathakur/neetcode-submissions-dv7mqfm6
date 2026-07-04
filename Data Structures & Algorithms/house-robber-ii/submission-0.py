class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(houses):
            rob1,rob2=0,0
            for n in houses:
                new_rob=max(n+rob1,rob2)
                rob1=rob2
                rob2=new_rob
            return rob2
        return max(helper(nums[:-1]),helper(nums[1:]))
        