class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=1
        suffix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*=suffix
            suffix*=nums[i]
        return res
        # output=[]
        # for i in range(len(nums)):
        #     left_prod=1
        #     right_prod=1
        #     for j in range(i):
                
        #         left_prod*=nums[j]
        #     for k in range(i+1,len(nums)):
                
        #         right_prod*=nums[k]
        #     output.append(left_prod*right_prod)
        
        # return output
            
           
        
        
        
       
