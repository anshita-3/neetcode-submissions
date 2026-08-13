class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones)>1:
            stones.sort(reverse=True)
            x=stones[0]
            y=stones[1]
            stones.pop(0)
            stones.pop(0)
            if x!=y:
                diff=x-y
                stones.append(diff)
        if stones:
            return stones[0]
        return 0
            
            