class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashset=set()
        i=0
        for n in nums:
            if n not in hashset:
                hashset.add(n)
                nums[i]=n
                i+=1
        return i
                        