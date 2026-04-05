class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(s,i):
            x=ord(s[i])
            if 97<=x<=122 or 48<=x<=57:
                return True
            return False
        s=s.lower()
        s=s.strip()
        n=len(s)
        i=0
        j=n-1
        while i<j:
            if not isAlpha(s,i):
                i+=1
                continue
            if not isAlpha(s,j):
                j-=1
                continue
            if s[i] == s[j]:
                i+=1
                j-=1
                
            else:
                return False
        return True        
     
               
         