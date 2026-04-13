class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) 
        max_get = [0]*n

        if n==1:
            return nums[0]
        
        max_get[0] = nums[0]
        max_get[1] = max(nums[1],nums[0])

        for i in range(2, n):
            max_get[i] = max(max_get[i-2]+nums[i],max_get[i-1])
        print(max_get)
        return max(max_get[-1], max_get[-2])
