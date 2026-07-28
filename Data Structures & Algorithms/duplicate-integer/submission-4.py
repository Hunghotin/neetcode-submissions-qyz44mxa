class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = set(nums)
        if len(mem) == len(nums):
            return False
        return True