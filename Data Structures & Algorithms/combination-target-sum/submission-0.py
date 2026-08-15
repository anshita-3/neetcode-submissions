class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        def backtrack(i,total):
            if total==target:
                res.append(path.copy())
                return
            if total>target:
                return 
            for j in range(i,len(nums)):
                path.append(nums[j])
                sum=total+nums[j]
                backtrack(j,sum)
                path.pop()
        backtrack(0,0)
        return res
        
