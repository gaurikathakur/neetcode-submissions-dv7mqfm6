class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = 0
        j = 0
        
        # 1. Merge characters alternately while both strings have letters
        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1
            
        # 2. Append any remaining characters from the longer string
        ans.append(word1[i:])
        ans.append(word2[j:])
        
        # 3. Join with an empty string, not a space
        return "".join(ans)
