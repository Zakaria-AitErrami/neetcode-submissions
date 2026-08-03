class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = list()
        for i,v in enumerate(nums):
            A.append([v,i])
        A.sort()
        i=0
        j=len(A)-1
        while i < j:
            if A[i][0]+A[j][0]==target:
                return sorted([A[i][1],A[j][1]])
            elif A[i][0]+A[j][0] < target:
                i+=1
            else:
                j-=1