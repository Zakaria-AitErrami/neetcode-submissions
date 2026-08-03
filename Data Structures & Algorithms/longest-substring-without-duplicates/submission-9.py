class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for L in range(len(s)):
            window = set()
            for R in range(L, len(s)):
                if s[R] in window:
                    break
                else:
                    window.add(s[R])
                    res = max(res, R-L+1)
        return res
