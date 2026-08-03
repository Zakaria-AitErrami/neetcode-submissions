class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(','{','[']
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if not stack:
                    return False
                item_before = stack.pop()
                if mapping[c] != item_before:
                    return False
        return  len(stack) == 0

        