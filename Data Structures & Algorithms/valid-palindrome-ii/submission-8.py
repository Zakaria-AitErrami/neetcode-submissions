class Solution:
    def validPalindrome(self, s: str) -> bool:
        # initalize L = 0
        # initializs R = len(s) - 1

        # loop while L <= R
        # compare s[L] and s[R]
        # we can either skipL or skip at right (skip = 0) 
        # skip var can be increamented to 1 maximum
        # cC => palidrom
        # abbda 
            # compare a with a
            # move both pointers L to the right and R to the left
            # skip L or skip R and compare if they are not equal
            # if skiped one time and they're not equal return False
        def isPalindrom(s):
            L, R = 0, len(s)-1
            while L <= R:
                if s[L] != s[R]:
                    return False
                L+=1
                R-=1
            return True
        L, R = 0, len(s) - 1
        while L <= R:
            if s[L] != s[R]:
                return isPalindrom(s[L+1:R+1]) or isPalindrom(s[L:R])
            L+=1
            R-=1
        return True
        