class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
        maps = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('z')] +=1
            maps[tuple(count)].append(s)
        return list(maps.values())