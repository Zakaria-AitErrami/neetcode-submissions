class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    res = a+b
                if token == '-':
                    res = a-b
                if token == '/':
                    res = int(a/b)
                if token == '*':
                    res = a*b
                stack.append(res)
        return stack[-1]