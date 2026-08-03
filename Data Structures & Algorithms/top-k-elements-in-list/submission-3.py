class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {} # key is the actual value and value is the freq 

        for i in nums:
            count[i] = count.get(i,0) + 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res