class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums = sorted(nums)
        res = 0
        count = 1
        last_num = nums[0]
        print(nums)
        for i in range(1,len(nums)):
            if nums[i]-last_num==0:
                continue
            if nums[i]-last_num==1:
                count+=1
                last_num = nums[i]
                print(nums[i],count)
            else:
                last_num = nums[i]
                res = max(res, count)
                count = 1
        res = max(res, count)
        return res