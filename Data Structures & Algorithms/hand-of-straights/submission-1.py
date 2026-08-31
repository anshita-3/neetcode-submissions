from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False 
        # freq={}
        # for i in hand:
        #     freq[i]=freq.get(0,i)+1
        count=Counter(hand)
        for i in sorted(count):
            while count[i]>0:
                for j in range(i,i+groupSize):
                    if count[j]==0:
                        return False 
                    count[j]-=1
        return True 
        