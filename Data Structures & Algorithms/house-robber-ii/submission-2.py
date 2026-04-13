class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_gain(num_list):
            n = len(num_list) 
            max_get = [0]*n
            
            if n==0:
                return 0
            if n==1:
                return num_list[0]
            
            max_get[0] = num_list[0]
            max_get[1] = max(num_list[1],num_list[0])

            for i in range(2, n):
                max_get[i] = max(max_get[i-2]+num_list[i],max_get[i-1])

            return max(max_get[-1], max_get[-2])
        if len(nums)==1:
            return nums[0]
        
        return max(max_gain(nums[:-1]), max_gain(nums[1:]))
