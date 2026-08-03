class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        visited = set()
        for i in range(len(strs)):
            items = list()
            if i in visited:
                continue
            items = [strs[i]]
            visited.add(i)
            for j in range(i+1,len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    items.append(strs[j])
                    visited.add(j)
            result.append(items)
        return result