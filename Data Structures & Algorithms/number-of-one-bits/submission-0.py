class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            num=n%2
            if num==1:
                count+=1
            n//=2
        return count
    #    return bin(n).count("1")

   