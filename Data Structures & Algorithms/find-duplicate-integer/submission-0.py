class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mem = []
        for num in nums:
            if num in mem:
                return num
            else:
                mem.append(num)