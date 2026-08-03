class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for number, rep in count.items():
            freq[rep].append(number)
        
        
        i = len(nums)
        while i > 0:
            if len(freq[i])!=0:
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
            i-=1
        return res