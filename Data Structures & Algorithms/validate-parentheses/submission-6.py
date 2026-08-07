class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", 
                    "[": "]", 
                    "{": "}"}

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif stack and brackets[stack.pop()] == c:
                continue
            else:
                return False
        
        if not stack:
            return True
        return False