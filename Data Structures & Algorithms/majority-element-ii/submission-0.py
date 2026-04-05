from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = Counter(nums)
        
        # Filter elements that appear more than n/3 times
        return [num for num, count in counts.items() if count > n // 3]
