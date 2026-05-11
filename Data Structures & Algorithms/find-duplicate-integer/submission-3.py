class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mem = {}
        for num in nums:
            mem[num] = mem.get(num,0)+1
            if mem[num]!=1:
                return num