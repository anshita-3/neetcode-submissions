class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[-num for num in stones]
        #now build heap
        heapq.heapify(maxheap)
        #now max heap is built
        while len(maxheap)>1:
            first=-heapq.heappop(maxheap)
            second=-heapq.heappop(maxheap)
            if first==second:
                continue
            if first!=second:
                new=first-second
                heapq.heappush(maxheap,-new)
        if maxheap:
            return -maxheap[0]
        return 0
        

