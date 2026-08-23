class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=set()
        total=0
        minheap=[(0,0)] #cost,point
        while len(visited)<n:
            cost,i=heapq.heappop(minheap)
            if i in visited:
                continue
            visited.add(i)
            total+=cost
            x1,y1=points[i]
            for j in range(n):
                if j not in visited:
                    x2,y2=points[j]
                    dist=abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(minheap,(dist,j))
        return total 
