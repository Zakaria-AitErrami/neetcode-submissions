class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        res = 0
        window = set()
        for R in range(len(s)):
            # shrink the window
            while s[R] in window:
                window.remove(s[L])
                L+=1
            # expand the window
            window.add(s[R])
            res = max(res, R-L+1)
        return res