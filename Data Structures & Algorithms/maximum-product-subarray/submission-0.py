class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('infinity')
        for i in range(len(nums)):
            tmp = 1
            for j in range(i, len(nums)):
                tmp*=nums[j]
                res = max(res, tmp)
        return res