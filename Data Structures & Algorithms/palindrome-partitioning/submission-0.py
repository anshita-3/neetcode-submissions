class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        substr=[]
        def dfs(i):
            if i==len(s):
                res.append(substr.copy())
                return
            for j in range(i,len(s)):
                word=s[i:j+1]
                if word==word[::-1]:
                    substr.append(word)
                    dfs(j+1)
                    substr.pop()
        dfs(0)
        return res
            
            
