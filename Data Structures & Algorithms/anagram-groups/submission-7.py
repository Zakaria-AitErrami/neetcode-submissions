class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = set()
        for i in range(len(strs)):
            item = [strs[i]]
            if i in seen:
                continue
            seen.add(i)
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    item.append(strs[j])
                    seen.add(j)
            res.append(item)
        return res
