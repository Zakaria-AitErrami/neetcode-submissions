class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L,R = 0,0
        count = dict()
        res = 0
        while R < len(s):
            # expand the window
            count[s[R]] = count.get(s[R],0) + 1
            # shrink the window
            while (R-L+1) - max(count.values()) > k:
                count[s[L]] = count.get(s[L],0) - 1
                L+=1
            res = max(res, R-L+1)
            R+=1
        return res
