class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = dict()
        countT = dict()

        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)