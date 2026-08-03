class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)):
            if i+len(s1) > len(s2):
                step = len(s2)
            else:
                step = i+len(s1)
            substr = sorted(s2[i:step])
            if s1 == substr:
                return True
            if step >= len(s2):
                break
        return False
