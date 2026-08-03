class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedword = ""
        for s in strs:
            encodedword += str(len(s)) + "#" +s
        return encodedword
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            strlen = int(s[i:j])
            res.append(s[j+1:j+strlen+1])
            i=j+strlen+1
        return res

            
            


