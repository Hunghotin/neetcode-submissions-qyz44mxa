class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mem = {}
        for i in nums:
            if i not in mem:
                mem[i]=1
            else:
                return True
        return False