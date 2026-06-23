class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        o_map={char: index for index, char in enumerate(order)}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    if o_map[w1[j]]> o_map[w2[j]]:
                        return False 
                    break 
            else:
                if len(w1)>len(w2):
                    return False 
        return True

                          