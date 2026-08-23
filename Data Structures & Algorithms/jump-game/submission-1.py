class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        last_index=n-1
        jump=nums[0]
        for i in range(1,len(nums)):
            if i>jump:
                return False 
            jump=max(jump,i+nums[i])
            if jump>=last_index:
                return True 
        return True 