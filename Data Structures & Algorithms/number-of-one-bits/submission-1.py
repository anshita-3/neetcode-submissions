class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            count+= n&1
            n>>=1
        return count
        # while n>0:
        #     num=n%2
        #     if num==1:
        #         count+=1
        #     n//=2
        # return count
    #    return bin(n).count("1")

   