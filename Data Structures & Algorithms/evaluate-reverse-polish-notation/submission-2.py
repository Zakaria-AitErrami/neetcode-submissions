class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        if len(tokens) == 1:
            return int(tokens[0]) 
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    res= a+b
                    stack.append(res)
                if token == '-':
                    res= a-b
                    stack.append(res)
                if token == '*':
                    res= a*b
                    stack.append(res)
                if token == '/':
                    res= a/b
                    stack.append(int(res))
        return stack[-1]

