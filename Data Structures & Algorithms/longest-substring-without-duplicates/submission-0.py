class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        longest = 0
        window = set()
        while R < len(s):    
            while s[R] in window:
                window.remove(s[L])
                L+=1
            window.add(s[R])
            longest = max(longest, len(window))
            R+=1
        return longest