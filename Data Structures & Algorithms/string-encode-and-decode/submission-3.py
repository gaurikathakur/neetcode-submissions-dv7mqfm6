class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # Store length, then a delimiter, then the string
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            # 1. Find the delimiter to get the length
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j]) # The number before '#'
            i = j + 1            # Move past '#'
            
            # 2. Read exactly 'length' characters
            res.append(s[i : i + length])
            i += length          # Move to the start of the next length prefix
            
        return res
