class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        n=len(nums)
        for n in nums:
            if n in hashset:
                return True 
            hashset.add(n)
        return False