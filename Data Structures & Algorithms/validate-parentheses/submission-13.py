class Solution:
    def isValid(self, s: str) -> bool:
        mapParentheses = {
            '(': ')',
            '[':']',
            '{':'}'
        }
        stack = []
        for c in s:
            if c in mapParentheses:
                stack.append(c)
            else:
                if not stack:
                    return False
                if mapParentheses[stack.pop()] != c:
                    return False
        return len(stack) == 0