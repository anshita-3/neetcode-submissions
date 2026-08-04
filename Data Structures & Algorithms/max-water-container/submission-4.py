class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        res=0
        while left<right:
            height=min(heights[left],heights[right])
            width=right-left
            water=width*height
            res=max(res,water)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return res


        # res=0
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         width=j-i
        #         height=min(heights[i],heights[j])
        #         water=width*height
        #         res=max(res,water)
        # return res
                
