class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            lenS = len(s)
            res += str(lenS) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            lenS = int(s[i:j])
            res.append(s[j+1:j+1+lenS])
            i = j+1+lenS
        return res