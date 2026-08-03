class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        arr = list()
        for num in nums:
            d[num] = d.get(num, 0)+1
        for key, value in d.items():
            arr.append([value,key])
        arr.sort(reverse=True)
        return [arr[i][1] for i in range(k)]