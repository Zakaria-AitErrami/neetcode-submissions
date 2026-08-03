class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))+'#'+s
        return res
    def decode(self, s: str) -> List[str]:
        res = list()
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j += 1
            lenstr = int(s[i:j])

            i=j+1
            j=lenstr+i
            res.append(s[i:j])
            i=j
        return res
