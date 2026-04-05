class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        end=len(nums)-1
        n=len(nums)
        k%=n
        def reverse(s: int, end: int):


            while s<end:

                nums[s],nums[end]=nums[end],nums[s]
                s+=1
                end-=1
        reverse(0, n - 1)
        # 2. Reverse the first k elements
        reverse(0, k - 1)
        # 3. Reverse the rest
        reverse(k,n-1)
        

        