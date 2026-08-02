class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=[]
        range_n=len(nums)
        for i in range(range_n+1):
            res.append(i)
        for i in range(range_n+1):
            if res[i] not in nums:
                return res[i]
       
            

        