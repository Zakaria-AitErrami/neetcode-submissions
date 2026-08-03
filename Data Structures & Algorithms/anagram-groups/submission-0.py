class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = list()
        visited = list()
        if len(strs) == 1:
            return [strs]
        for i,s in enumerate(strs):
            if sorted(s) in visited:
                continue
            l = list()
            l.append([s])
            visited.append(sorted(s))
            for j in range(i+1, len(strs)):
                if sorted(s) == sorted(strs[j]):
                    l[0].append(strs[j])
            res.extend(l)
        return res
