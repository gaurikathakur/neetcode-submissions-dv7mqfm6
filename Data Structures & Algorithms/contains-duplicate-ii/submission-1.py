class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = {} # Use a dictionary to store {number: index}
        n = len(nums)
        i = 0
        
        while i < n:
            # 1. Check if the current number was seen before
            if nums[i] in hashset:
                j = hashset[nums[i]] # Get the index 'j' of the previous occurrence
                
                # 2. Check if the distance between current i and previous j is <= k
                if abs(i - j) <= k:
                    return True
            
            # 3. Always update the hashset with the latest index of this number
            hashset[nums[i]] = i
            
            # 4. Move to the next index
            i += 1
            
        return False
