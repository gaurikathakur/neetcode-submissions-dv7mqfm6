import math 
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        ans=r
        while l<=r:
            mid=(l+r)//2
            curr_weight=0
            needed_days=1
            for w in weights:
                if curr_weight+w > mid:
                    needed_days+=1
                    curr_weight=0
                curr_weight+=w
            if needed_days<=days:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans 