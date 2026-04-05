class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        record=[]
        for token in tokens:
            if token in "+*/-":

                b=record.pop()
                a=record.pop()
                if token=='+':
                    record.append(a+b)
                elif token=='-':
                    record.append(a-b)
                elif token=='*':
                    record.append(a*b)
                elif token=='/':
                    record.append(int(a/b))
            else:
                record.append(int(token))
        return record[0]



                


        