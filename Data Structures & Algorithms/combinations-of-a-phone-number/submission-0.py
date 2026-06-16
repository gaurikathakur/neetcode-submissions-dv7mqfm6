class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_letter={
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"

        }
        res=[]
        def backtrack(i,curr):
            if len(curr)==len(digits):
                res.append("".join(curr))
                return 
            curr_digit=digits[i]
            letters=digit_letter[curr_digit]
            for letter in letters:
                curr.append(letter)
                backtrack(i+1,curr)
                curr.pop()
        backtrack(0,[])
        return res


            
        