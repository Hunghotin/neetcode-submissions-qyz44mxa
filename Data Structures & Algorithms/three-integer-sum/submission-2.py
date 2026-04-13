class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums = sorted(nums)
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                    continue
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                    continue
                else: 
                    tmp = sorted([nums[i],nums[j],nums[k]])
                    if tmp not in result:
                        result.append(tmp)
                    j+=1
        return result