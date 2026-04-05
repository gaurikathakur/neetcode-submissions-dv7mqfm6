class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        results = []
        
        for i in range(n - 3):
            # Optimization 1: Current smallest sum is too large
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: break
            # Optimization 2: Current largest sum is too small
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target: continue
            
            if i > 0 and nums[i] == nums[i-1]: continue
            
            for j in range(i + 1, n - 2):
                # Optimization 3: Similar checks for the second loop
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target: break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target: continue
                
                if j > i + 1 and nums[j] == nums[j-1]: continue
                
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]: left += 1
                        while left < right and nums[right] == nums[right-1]: right -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return results
