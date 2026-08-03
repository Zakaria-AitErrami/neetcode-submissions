class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = dict()
        countT = dict()

        if len(s) != len(t):
            return False
        
        for i,j in zip(s,t):
            countS[i] = countS.get(i,0) +1
            countT[j] = countT.get(j,0) +1
        return countS == countT