class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            a=-(heapq.heappop(maxheap))
            b=-(heapq.heappop(maxheap))
            if a==b:
                continue
            elif a!=b:
                diff=a-b
                heapq.heappush(maxheap,-diff)
        if maxheap:
            return -maxheap[0]
        return 0