class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # 1. Sort the strings alphabetically
        strs.sort()
        
        # 2. Compare only the first and the last string
        first = strs[0]
        last = strs[-1]
        i = 0
        
        # 3. Find the matching characters at the start
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        return first[:i]