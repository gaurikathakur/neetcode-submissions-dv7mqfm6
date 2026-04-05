class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        
        # 2. Sort the entire array in-place
        nums1.sort()