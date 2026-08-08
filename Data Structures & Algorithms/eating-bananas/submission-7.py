class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        res=right
        while left<=right:
            k=(left+right)//2
            hrs=0
            for pile in piles:
                hrs+=math.ceil(pile/k)
            if hrs<=h:
                res=k
                right=k-1
            else:
                left=k+1
        return res 
        # k=1
        # while True:
        #     hrs=0
        #     for pile in piles:
        #         hrs+=math.ceil(pile/k)
        #     if hrs<=h:
        #         return k 
        #     k+=1
        # return k

        # k=1
        # while True:
        #     hrs=0
        #     for pile in piles:
        #         temp=pile
        #         while temp>0:
        #             temp-=k
        #             hrs+=1
        #     if hrs<=h:
        #         return k 
        #     k+=1
        