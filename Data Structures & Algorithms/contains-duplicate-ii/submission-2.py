class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset={}
        n=len(nums)
        i=0
        while i<n:
            if nums[i] in hashset:
                j=hashset[nums[i]]
                if abs(i-j)<=k:
                    return True
            hashset[nums[i]]=i
            i+=1
        return False