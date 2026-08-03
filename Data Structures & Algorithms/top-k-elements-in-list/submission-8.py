class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for num in nums:
            d[num] = 1 + d.get(num,0)
        cnt = []
        for key,v in d.items():
            cnt.append([v,key])
        cnt.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(cnt[i][1])
        return res