class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Option 1: Skip s[left]
                skip_left = s[left + 1 : right + 1]
                # Option 2: Skip s[right]
                skip_right = s[left : right]
                
                # Check if either substring is a palindrome
                return (skip_left == skip_left[::-1] or 
                        skip_right == skip_right[::-1])
            
            left += 1
            right -= 1
            
        return True

        