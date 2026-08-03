class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]

        for i in range(len(nums)):
            left_prod=1
            right_prod=1
            for j in range(i):
                
                left_prod*=nums[j]
            for k in range(i+1,len(nums)):
                
                right_prod*=nums[k]
            output.append(left_prod*right_prod)
        
        return output
            
           
        
        
        
       
