class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currentsum=nums[0]
        for i in range(1,len(nums)):
            currentsum=max(currentsum+nums[i],nums[i])
            maxsum=max(currentsum,maxsum) 
        return maxsum
            