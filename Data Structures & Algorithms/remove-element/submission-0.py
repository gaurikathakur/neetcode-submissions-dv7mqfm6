class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for i in range(len(nums)):
            # Only add the numbers we want to keep
            if nums[i] != val:
                ans.append(nums[i])
        
        # To pass LeetCode, you MUST copy these back into 'nums'
        for i in range(len(ans)):
            nums[i] = ans[i]
            
        return len(ans)