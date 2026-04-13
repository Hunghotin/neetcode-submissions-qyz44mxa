class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        flag = False
        count = 0
        for num in nums:
            if num!=0:
                p *= num
            else:
                count+=1
                flag = True
        if count>=2:
            p = 0
        
        result = [p]*len(nums)
        for i in range(len(result)):
            if flag:
                if nums[i]!=0:
                    result[i]=0
            else:
                result[i]=int(result[i]/nums[i])
        return result
