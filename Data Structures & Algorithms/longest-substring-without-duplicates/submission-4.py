class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        longest=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            longest=max(longest,len(seen))
        return longest 
            

        # longest=0
        # for i in range(len(s)):
        #     seen=set()
        #     for j in range(i,len(s)):
        #         if s[j] in seen:
        #             break 
        #         seen.add(s[j])
        #         longest=max(longest,len(seen))
        # return longest 
                