class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = dict()
        arr = list()
        result = list()
        # number -> frequency
        for num in nums:
            map[num] = map.get(num,0) + 1
        
        for number, frequency in map.items():
            arr.append([frequency, number])
        
        arr.sort(reverse=True)
    
        for i in range(k):
            result.append(arr[i][1])
        return result
        