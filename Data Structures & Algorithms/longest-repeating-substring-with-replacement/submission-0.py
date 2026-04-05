class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        hashset = set(s)
        
        for char in hashset:
            # Everything below this line should be indented (one tab in)
            left = 0
            replacements_used = 0
            for right in range(len(s)):
                if s[right] != char:
                    replacements_used += 1
                
                while replacements_used > k:
                    if s[left] != char:
                        replacements_used -= 1 
                    left += 1
                
                ans = max(ans, right - left + 1)
        
        return ans
