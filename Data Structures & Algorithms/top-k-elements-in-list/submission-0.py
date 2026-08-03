class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        keys = list()
        for num in nums:
            d[num] = d.get(num, 0)+1
        values = sorted(d.values(), reverse=True)
        for v in values:
            for key,value in d.items():
                if v==value and key not in keys:
                    keys.append(key)
        return keys[:k]