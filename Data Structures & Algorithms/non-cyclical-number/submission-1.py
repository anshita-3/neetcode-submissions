class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            sum=0
            while n>0:
                digit=n%10
                n//=10
                sq=digit*digit
                sum+=sq
            n=sum
        return True