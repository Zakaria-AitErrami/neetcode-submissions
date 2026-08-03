class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = dict()
        for num in nums:
            freqMap[num] = freqMap.get(num,0) + 1
        res = []
        for num, freq in freqMap.items():
            res.append([freq, num])
        
        res.sort(reverse=True)
        return [n[1] for n in res[:k]]


            