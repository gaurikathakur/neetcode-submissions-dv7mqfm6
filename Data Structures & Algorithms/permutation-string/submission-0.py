from collections import Counter 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        for i in range(n1,n2):
            if n1>n2:
                return False 
        s1_counts=Counter(s1)
        windows_counts=Counter(s2[:n1])
        if s1_counts==windows_counts:
            return True 
        for i in range(n1,n2):

            entering=s2[i]
            windows_counts[entering]+=1 
            leaving=s2[i-n1]
            if windows_counts[leaving]==1:
                del windows_counts[leaving]
            else:
                windows_counts[leaving]-=1
            if s1_counts==windows_counts:
                return True 
        return False



