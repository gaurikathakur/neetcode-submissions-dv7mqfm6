class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            curr_sum=0
            subarrays=1
            for num in nums:
                if curr_sum+num>max_sum:
                    subarrays +=1
                    curr_sum=num 
                else:
                    curr_sum+= num  
            return subarrays<=k
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            if can_split(mid):
                result=mid 
                high=mid-1
            else:
                low=mid+1
        return result