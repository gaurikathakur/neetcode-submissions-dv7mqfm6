class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Arrange them in order
        result = []

        for i in range(len(nums)):
            # Don't pick the same starting number twice
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Look for the other two numbers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1 # Need a bigger number
                elif total > 0:
                    right -= 1 # Need a smaller number
                else:
                    # Found a match!
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    # Skip same numbers for the 'left' pointer too
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                        
        return result
        