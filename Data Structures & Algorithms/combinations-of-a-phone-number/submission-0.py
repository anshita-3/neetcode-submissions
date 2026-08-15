class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        pairs={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        subset=[]
        def dfs(i):
            if i==len(digits):
                res.append("".join(subset))
                return 
            for letter in pairs[digits[i]]:
                subset.append(letter)
                dfs(i+1)
                subset.pop()
            # for i in range(len(digits)):
            #     subset.append("".join(pairs[i]))
            #     dfs(i)
            #     subset.pop()
        dfs(0)
        return res 