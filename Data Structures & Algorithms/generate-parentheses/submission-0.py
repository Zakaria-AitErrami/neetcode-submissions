class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def isValid(s):
            o = 0
            if not s.startswith("("):
               return False
            for c in s:
                o+=1 if c == '(' else -1
                if o < 0:
                    return False
            return not o
        def backtrack(s):
            if n*2 == len(s):
                if isValid(s):
                    res.append(s)
                return
            
            for choice in ["(",")"]:

                backtrack(s+choice)
                
            
        

        backtrack("")
        return res