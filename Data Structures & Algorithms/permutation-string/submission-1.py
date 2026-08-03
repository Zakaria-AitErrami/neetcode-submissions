class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for L in range(len(s2)):
            for R in range(L, min(len(s2), L+len(s1))):
                substr = sorted(s2[L: R+1])
                if substr == s1:
                    return True
        return False