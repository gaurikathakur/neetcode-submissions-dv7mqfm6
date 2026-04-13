class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # We want to binary search on the smaller array for O(log(min(n,m)))
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r) // 2  # A's partition index
            j = half - i - 2  # B's partition index
            
            # Boundary checks for A
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            
            # Boundary checks for B
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Check if we have a valid partition
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total length
                if total % 2:
                    return min(Aright, Bright)
                # Even total length
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                # A's partition is too big, move left
                r = i - 1
            else:
                # A's partition is too small, move right
                l = i + 1
