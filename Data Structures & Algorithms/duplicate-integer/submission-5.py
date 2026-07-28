class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for i in range(len(nums)):
            if nums[i] not in cache:
                cache[nums[i]] = 1
            else:
                return True
        return False
        