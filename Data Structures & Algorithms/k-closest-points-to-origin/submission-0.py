class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        heapq.heapify(ans)
        for i in range(len(points)):
            dist=math.sqrt((points[i][0])**2+(points[i][1]**2))
            heapq.heappush(ans,(dist,points[i]))
        res=[]
        for i in range(k):
            dist,point=heapq.heappop(ans)
            res.append(point)
        return res
      


