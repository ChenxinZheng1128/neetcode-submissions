class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(': ")",
            '[': ']',
            '{': '}'
        }

        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                if brackets[stack.pop()] != c:
                    return False
        
        return not stack