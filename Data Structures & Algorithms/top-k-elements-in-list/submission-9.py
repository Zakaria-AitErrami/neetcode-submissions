class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nbr -> frequency
        # [ [Frequency, nbr], .... ] sort reverse = true
        countNum = dict()
        for num in nums:
            countNum[num] = countNum.get(num,0) + 1
        res = []
        for nbr, freq in countNum.items():
            res.append([freq,nbr])
        
        res.sort(reverse=True)
        return [nbr for freq, nbr in res[:k]]