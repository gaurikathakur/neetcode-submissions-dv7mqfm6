import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=(l+r)//2
            total_hours=0
            for p in piles:
                 total_hours += math.ceil(p / mid)
            
            # 3. Adjust search based on total time spent
            if total_hours <= h:
                ans = mid      # This speed works! 
                r = mid - 1    # Can we go even slower?
            else:
                l = mid + 1    # Too slow, must increase speed
                
        return ans

        