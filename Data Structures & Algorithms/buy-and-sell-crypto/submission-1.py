class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof={0}
        profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=max(0,prices[j]-prices[i])
                prof.add(profit)
        return max(prof)
