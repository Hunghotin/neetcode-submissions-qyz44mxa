class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                if a+b==target:
                    return [i,j]
        