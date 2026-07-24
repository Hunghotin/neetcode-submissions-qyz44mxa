class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lst_jmp = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=lst_jmp:
                lst_jmp = i
        
        if lst_jmp!=0:
            return False
        else:
            return True