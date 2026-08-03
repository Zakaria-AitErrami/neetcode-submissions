class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict = dict()
        tDict = dict()
        for c in s:
            sDict[c] = 1 + sDict.get(c, 0)
        for c in t:
            tDict[c] = 1 + tDict.get(c, 0)  
        return tDict == sDict
        