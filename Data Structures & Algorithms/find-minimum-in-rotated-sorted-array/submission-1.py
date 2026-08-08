class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums.sort()
        # mini=nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i-1]>nums[i]:
        #         mini=nums[i]
        # return mini
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]

        #return min(nums)
