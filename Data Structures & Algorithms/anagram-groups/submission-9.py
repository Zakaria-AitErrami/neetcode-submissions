class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagraDict = defaultdict(list)
        res = []
        for s in strs:
            anagraDict[tuple(sorted(s))].append(s)
        
        for k, v in anagraDict.items():
            res.append(v)
        return res
        