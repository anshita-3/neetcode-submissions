class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i,n in enumerate(numbers):
            diff=target-n
            if diff in hashmap:
                return [hashmap[diff]+1,i+1]
            hashmap[n]=i
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return[i+1,j+1]

    