class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        visited = set()
        for i in range(len(strs)):
            items = [strs[i]]
            if i in visited:
                continue
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    items.append(strs[j])
                    visited.add(j)
            result.append(items)
            visited.add(i)
            items = list()
        return result
            