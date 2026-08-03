class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L, R = 0,0
        longest = 0
        while R < len(s):

            # shrink the window
            while s[R] in charSet:
                charSet.remove(s[L])
                L+=1
            charSet.add(s[R])
            longest = max(longest, R-L+1)
        
            R+=1
        return longest