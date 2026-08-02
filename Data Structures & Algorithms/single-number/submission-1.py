class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # seen=set()
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #        seen.remove(nums[i])
        #     else:
        #         seen.add(nums[i])
        # return seen.pop()

        # count={}
        # for i in range(len(nums)):
        #     count[nums[i]]=count.get(nums[i],0)+1
        # for num in count:
        #     if count[num]==1:
        #         return num

        res=0
        for i in range(len(nums)):
            res^=nums[i]
        return res