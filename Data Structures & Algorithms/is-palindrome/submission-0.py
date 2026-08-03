class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        s = ''.join(c.lower() for c in s if c.isalnum())
        R = len(s)-1
        while L < R:
            if s[L] != s[R]:
                return False
            L+=1
            R-=1
        return True

        