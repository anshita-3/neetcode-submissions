class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        candidates.sort()
        def backtrack(i,total):
            if total==target:
                res.append(path.copy())
            if total>target:
                return 
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if total+candidates[j]>target:
                    break
                path.append(candidates[j])
                sum=total+candidates[j]
                backtrack(j+1,sum)
                path.pop()
        backtrack(0,0)
        return res