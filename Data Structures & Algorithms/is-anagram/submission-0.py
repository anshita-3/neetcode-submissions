class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s={}
        letters_t={}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            letters_s[s[i]]=1+ letters_s.get(s[i],0)
            letters_t[t[i]]=1+ letters_t.get(t[i],0)
        
        return letters_s==letters_t
        