class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_weight=sum(stones)
        target=total_weight//2
        dp=[False]*(target+1)
        dp[0]=True 
        for stone in stones:
            for j in range(target,stone-1,-1):
                if dp[j-stone]:
                    dp[j]=True 
        for s in range(target,-1,-1):
            if dp[s]:
                return total_weight-2*s
        return 0
                


        