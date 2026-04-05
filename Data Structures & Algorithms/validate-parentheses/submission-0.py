class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Map closing brackets to their matching opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # 2. If it's a closing bracket
            if char in mapping:
                # Pop the top of the stack (if empty, use a dummy value '#')
                top_element = stack.pop() if stack else '#'
                
                # 3. If it doesn't match the mapped opening bracket, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # 4. It's an opening bracket, so push it onto the stack
                stack.append(char)

        # 5. If the stack is empty, all brackets were matched perfectly
        return not stack
