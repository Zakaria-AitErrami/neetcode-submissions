class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def isValid(s):
            open = 0
            for c in s:
                open+=1 if c== '(' else -1
                if open < 0:
                    return False
            return not open
        
        def backtrack(s):
            if len(s) == n*2:
                if isValid(s):
                    res.append(s)
                return

            for choice in ['(',')']:
                backtrack(s+choice)
        backtrack("")
        return res