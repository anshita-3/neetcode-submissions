class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volumes=set()
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                width=j-i
                height=min(heights[i],heights[j])
                water=width*height
                volumes.add(water)
        return max(volumes)

    