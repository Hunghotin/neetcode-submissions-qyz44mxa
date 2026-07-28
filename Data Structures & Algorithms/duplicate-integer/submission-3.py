class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for i in nums:
            if i not in mem:
                mem.add(i)
            else:
                return True
        return False